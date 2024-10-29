from datetime import datetime
from typing import Union, List

from k2magic.dataframe_db_exception import DataFrameDBException
from sqlalchemy import URL, make_url, create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from d3sdk.model.device_failure_record import DeviceFailureRecord, Fm
from d3sdk.model.alarm_group_detail import AlarmGroupDetail, Step, Cause


class D3DataFrameDB:
    """
    基于K2DataFrameDB，提供根据业务信息如报警组访问K2Assets Repo数据的能力
    :param k2a_url: k2a地址
    :param debug: 调试模式可输出更多日志信息
    """

    def __init__(self, k2a_url: Union[str, URL], debug: bool = False,):


        k2a_url_obj = make_url(k2a_url)
        # PG数据库信息，暂时写死，未来应从k2a获取 (TODO)
        pg_host = k2a_url_obj.host
        pg_port = 5432
        pg_user = 'k2data'
        pg_password = 'K2data1234'

        pg_url_obj = make_url(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/default')
        self.engine = create_engine(pg_url_obj, echo=debug)
        # self.k2DataFrameDB = K2DataFrameDB(k2a_url, schema=schema, db_port=db_port, debug=debug, rest=rest)

    def getDeviceFailureRecords(self, start_time_1: Union[str, int, datetime], end_time_1: Union[str, int, datetime],
                                start_time_2: Union[str, int, datetime], end_time_2: Union[str, int, datetime],
                      devices: list = None, limit: int = None, desc: bool = None) -> List[DeviceFailureRecord]:
        """
        -- 1.1 报警组列表查询（包括报警信息、相关争端模块列表）
        -- 查询获取报警组关联的报警类型、报警描述、报警数、严重程度、报警位置等业务信息
        -- 根据时间范围和设备信息、报警位置等信息查询获取符合要求的报警组编号
        -- 查询参数可选为：机组编码、报警组编码、诊断模块实例名称、报警组状态、报警等级、最早报警时间范围、最新报警时间范围、关键字、报警描述
        """
        if isinstance(start_time_1, str):
            start_time_1 = datetime.strptime(start_time_1, "%Y-%m-%d %H:%M:%S")
        if isinstance(end_time_1, str):
            end_time_1 = datetime.strptime(end_time_1, "%Y-%m-%d %H:%M:%S")
        if isinstance(start_time_2, str):
            start_time_2 = datetime.strptime(start_time_2, "%Y-%m-%d %H:%M:%S")
        if isinstance(end_time_2, str):
            end_time_2 = datetime.strptime(end_time_2, "%Y-%m-%d %H:%M:%S")

        sql = f"""
        SELECT
            ag.dfem_code,	-- 报警组编码（唯一标识）
            ag.display_name, -- 报警组名称
            CASE 
                WHEN ag.dfem_bjlx ILIKE '%symptom%' THEN 'symptom'
                WHEN ag.dfem_bjlx ILIKE '%failure%' THEN 'failure'
                ELSE ag.dfem_bjlx
          END as dfem_bjlx,	-- 报警类型
            ag.dfem_sxmsbh,	-- 报警编码
            ag.description,	--报警描述
            ag.dfem_bjs,	-- 报警数
            ag.dfem_bjdj,	--报警等级
            ag.dfem_zt,	-- 报警状态
            ag.dfem_gjz,	--关键字
            to_char(ag.dfem_zzbjsj, 'YYYY-MM-DD HH24:MI:SS') dfem_zzbjsj, -- 最早报警时间
            to_char(ag.dfem_zxbjsj, 'YYYY-MM-DD HH24:MI:SS') dfem_zxbjsj,	-- 最新报警时间
            -- ai.ID AS ai_id,  -- 设备ID
            ai.NAME AS device_code, -- 机组编码
            -- fmt.ID AS fmt_id, -- 诊断模块类型ID
            -- fmt.dfem_code AS fmt_code, -- 诊断模块类型编码
            -- fmt.display_name AS fmt_name,	-- 诊断模块类型名称
            -- fm.ID AS fm_id, -- 诊断模块实例ID
            fm.dfem_gnmkbh AS fm_code, -- 诊断模块实例编码（报警:诊断模块实例 1:n）
            fm.display_name AS fm_name -- 诊断模块实例名称
        FROM
            dfem_alarm_group ag
            -- 征兆类型报警组
            LEFT JOIN dfem_sign s ON s.dfem_code = ag.dfem_sxmsbh AND ag.dfem_bjlx ILIKE '%symptom%'
            -- 失效类型报警组
            LEFT JOIN dfem_failure_mode f ON f.dfem_code = ag.dfem_sxmsbh AND ag.dfem_bjlx ILIKE '%failure%'
            -- 诊断模块类型和征兆的关联
            LEFT JOIN dfem_rt_fm_sg fs ON fs.entity_type2_id = s.ID AND ag.dfem_bjlx ILIKE '%symptom%'
            -- 诊断模块类型和失效的关联
            LEFT JOIN dfem_rt_fmt_fm ff ON ff.entity_type2_id = f.ID AND ag.dfem_bjlx ILIKE '%failure%'
          -- 诊断模块类型
            LEFT JOIN dfem_functional_module_type fmt ON fmt.ID = ff.entity_type1_id or fmt.ID = fs.entity_type1_id
            LEFT JOIN asset_instances ai ON ai.ID = CAST ( ag.dfem_sbbh AS NUMERIC )
            -- 诊断模块实例
            LEFT JOIN dfem_functional_module fm ON fm.ID = ( SELECT fmt1.entity_type2_id FROM dfem_rt_fmt_fm1 fmt1 WHERE fmt1.entity_type1_id = fmt.ID AND fmt1.entity_type2_id = fm.ID ) 
        WHERE 1=1
            and ai.name in ({','.join(f"'{d}'" for d in devices)}) -- 参数：机组编码
            -- and ag.dfem_code = 'AG0000121409'	-- 参数：报警组编码
            and fm.display_name in ('定子', '转子绝缘', '定子绕组温度') -- 参数：诊断模块实例名称
            and ag.dfem_zt in ('已查看', '密切监视') -- 参数：报警组状态
            and ag.dfem_bjdj in ('注意')	-- 参数：报警等级
            and ag.dfem_zzbjsj BETWEEN '{start_time_1.strftime('%Y-%m-%d %H:%M:%S')}' AND '{end_time_1.strftime('%Y-%m-%d %H:%M:%S')}' -- 参数：最早报警时间范围
            and ag.dfem_zxbjsj BETWEEN '{start_time_2.strftime('%Y-%m-%d %H:%M:%S')}' AND '{end_time_2.strftime('%Y-%m-%d %H:%M:%S')}' -- 参数：最新报警时间范围
            -- and ag.dfem_gjz like '%%'	-- 参数：关键字
            -- and (ag.description like '%%' or ag.display_name like '%%')	-- 参数：报警描述
        ORDER BY ag.dfem_code {'desc' if desc else 'asc'}, ag.dfem_zzbjsj {'desc' if desc else 'asc'}
	    """

        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(sql))
                records = []
                last_record = None
                for row in result.fetchall():
                    fm = Fm(row[12], row[13])
                    if last_record is not None and last_record.dfem_code == row[0]:
                        last_record.fms.append(fm)
                    else:
                        record = DeviceFailureRecord(
                            dfem_code=row[0],
                            display_name=row[1],
                            dfem_bjlx=row[2],
                            dfem_sxmsbh=row[3],
                            description=row[4],
                            dfem_bjs=row[5],
                            dfem_bjdj=row[6],
                            dfem_zt=row[7],
                            dfem_gjz=row[8],
                            dfem_zzbjsj=row[9],
                            dfem_zxbjsj=row[10],
                            device_code=row[11],
                            fms=[fm],
                        )
                        records.append(record)
                        last_record = record
                return records
        except SQLAlchemyError as e:
            raise DataFrameDBException(
                "Failed to query records due to a database error.",
                original_exception=e
            )

    def getFailureCodes(self, dfem_code: str) -> List[AlarmGroupDetail]:
        """
        -- 1.2 根据报警组编号查询获取报警组关联的业务对象实例，如征兆、失效、原因、建议编码等
        """

        sql = f"""
        SELECT 
            ag.dfem_sxmsbh, -- 报警编码
            CASE 
                WHEN ag.dfem_bjlx ILIKE '%symptom%' THEN 'symptom'
                WHEN ag.dfem_bjlx ILIKE '%failure%' THEN 'failure'
                ELSE ag.dfem_bjlx
          END as dfem_bjlx, -- 报警类型
            cause.dfem_sxyybh cause_code, -- 原因编码 （报警:原因 1:n）
            cause.display_name cause_display_name, -- 原因名称
            cause.description cause_description,	-- 原因描述
            step.dfem_csbh step_code, -- 建议编号（原因:建议 1:n）
            step.display_name step_display_name, 	-- 建议名称
            step.description step_description -- 建议描述
        FROM
            dfem_alarm_group ag
            -- 征兆类型报警组
            LEFT JOIN dfem_sign s ON s.dfem_code = ag.dfem_sxmsbh AND ag.dfem_bjlx ILIKE '%symptom%'
            -- 失效类型报警组
            LEFT JOIN dfem_failure_mode f ON f.dfem_code = ag.dfem_sxmsbh AND ag.dfem_bjlx ILIKE '%failure%'
            -- 征兆和原因的关联
            LEFT JOIN dfem_rt_si_fc sf ON sf.entity_type1_id = s.ID AND ag.dfem_bjlx ILIKE '%symptom%'
            -- 失效和原因的关联
            LEFT JOIN dfem_rt_fm_fc ff ON ff.entity_type1_id = f.ID AND ag.dfem_bjlx ILIKE '%failure%'
          -- 原因
            LEFT JOIN dfem_failurecause cause ON cause.ID = sf.entity_type2_id or cause.ID = ff.entity_type2_id
            LEFT JOIN dfem_rt_fc_st fs on fs.entity_type1_id = cause.id
            LEFT JOIN dfem_step step on step.id = fs.entity_type2_id
        WHERE ag.dfem_code = '{dfem_code}'
        ORDER BY ag.dfem_sxmsbh, cause_code, step_code
        """

        try:
            with (self.engine.connect() as conn):
                result = conn.execute(text(sql))
                records = []
                last_record: AlarmGroupDetail = None
                last_cause: Cause = None
                for row in result.fetchall():
                    dfem_sxmsbh = row[0]
                    cause_code = row[2]
                    step_code = row[5]
                    step = Step(step_code, row[6], row[7])
                    same_sxmsbh = last_record is not None and last_record.dfem_sxmsbh == dfem_sxmsbh
                    same_cause = last_cause is not None and last_cause.code == cause_code

                    if same_sxmsbh:
                        if same_cause:
                            last_cause.steps.append(step)
                        else:
                            cause = Cause(cause_code, row[3], row[4], [step])
                            last_record.causes.append(cause)
                            last_cause = cause
                    else:
                        cause = Cause(cause_code, row[3], row[4], [step])
                        last_cause = cause
                        record = AlarmGroupDetail(
                            dfem_sxmsbh=dfem_sxmsbh,
                            dfem_bjlx=row[1],
                            causes=[cause],
                        )
                        records.append(record)
                        last_record = record

                return records
        except SQLAlchemyError as e:
            raise DataFrameDBException(
                "Failed to query records due to a database error.",
                original_exception=e
            )
