r"""Script to run through a processing task with the processor class.

Run command:

cd .\prototypes\dissolved_oxygen
streamlit run .\do_script.py

"""

import pandas as pd
import streamlit as st

import hydrobot
from hydrobot.data_acquisition import (
    import_inspections,
    import_ncr,
    import_prov_wq,
)
from hydrobot.do_processor import DOProcessor
from hydrobot.filters import trim_series
from hydrobot.plotter import make_processing_dash
from hydrobot.utils import merge_all_comments

#######################################################################################
# Reading configuration from config.yaml
#######################################################################################

data, ann = DOProcessor.from_config_yaml("do_config.yaml")

st.set_page_config(
    page_title="Hydrobot" + hydrobot.__version__, layout="wide", page_icon="💦"
)
st.title(f"{data.site}")
st.header(f"{data.standard_measurement_name}")

#######################################################################################
# Importing all check data that is not obtainable from Hilltop
# (So far Hydrobot only speaks to Hilltop)
#######################################################################################

check_col = "Value"
logger_col = "Logger"

inspections = import_inspections(
    "DO_Inspections.csv", check_col=check_col, logger_col=logger_col
)
prov_wq = import_prov_wq(
    "DO_ProvWQ.csv", check_col=check_col, logger_col=logger_col, use_for_qc=True
)
ncrs = import_ncr("DO_non-conformance_reports.csv")
inspections_no_dup = inspections.drop(data.check_data.index, errors="ignore")
prov_wq_no_dup = prov_wq.drop(data.check_data.index, errors="ignore")

all_checks_list = [data.check_data, inspections, prov_wq]
all_checks_list = [i for i in all_checks_list if not i.empty]

all_checks = pd.concat(all_checks_list).sort_index()

all_checks = all_checks.loc[
    (all_checks.index >= data.from_date) & (all_checks.index <= data.to_date)
]

# For any constant shift in the check data, default 0
# data.quality_code_evaluator.constant_check_shift = -1.9
check_data_list = [data.check_data, inspections_no_dup, prov_wq_no_dup]
check_data_list = [i for i in check_data_list if not i.empty]
data.check_data = pd.concat(check_data_list).sort_index()

data.check_data = data.check_data.loc[
    (data.check_data.index >= data.from_date) & (data.check_data.index <= data.to_date)
]

all_comments = merge_all_comments(data.check_data, prov_wq, inspections, ncrs)

#######################################################################################
# Common auto-processing steps
#######################################################################################

data.pad_data_with_nan_to_set_freq()

# Clipping all data outside of low_clip and high_clip
data.clip()

# Remove obvious spikes using FBEWMA algorithm
data.remove_spikes()

#######################################################################################
# DO specific operation
#######################################################################################

data.correct_do()

#######################################################################################
# INSERT MANUAL PROCESSING STEPS HERE
# Remember to add Annalist logging!
#######################################################################################

# Manually removing an erroneous check data point
# ann.logger.info(
#     "Deleting SOE check point on 2023-10-19T11:55:00. Looks like Darren recorded the "
#     "wrong temperature into Survey123 at this site."
# )
# data.check_series = pd.concat([data.check_series[:3], data.check_series[9:]])

#######################################################################################
# Assign quality codes
#######################################################################################
data.quality_encoder()
data.standard_data["Value"] = trim_series(
    data.standard_data["Value"],
    data.check_data["Value"],
)

# ann.logger.info(
#     "Upgrading chunk to 500 because only logger was replaced which shouldn't affect "
#     "the temperature sensor reading."
# )
# data.quality_series["2023-09-04T11:26:40"] = 500

#######################################################################################
# Export all data to XML file
#######################################################################################
data.data_exporter()
# data.data_exporter("hilltop_csv", ftype="hilltop_csv")
# data.data_exporter("processed.csv", ftype="csv")

#######################################################################################
# Launch Hydrobot Processing Visualiser (HPV)
# Known issues:
# - No manual changes to check data points reflected in visualiser at this point
#######################################################################################
fig = data.plot_qc_series(show=False)

fig_subplots = make_processing_dash(
    fig,
    data,
    all_checks,
)

st.plotly_chart(fig_subplots, use_container_width=True)

st.dataframe(all_comments, use_container_width=True)
# st.dataframe(data.standard_data, use_container_width=True)
st.dataframe(data.check_data, use_container_width=True)
st.dataframe(data.quality_data, use_container_width=True)
