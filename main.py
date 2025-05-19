import streamlit as st
from pint import UnitRegistry

ureg =UnitRegistry()
st.title("Unit Converter")

categories ={
    "Length" :["meter","centimeter","kilometer"],
    "Weight":["kilogram","milligram","gram"],
    "Temperature":["celsius","fahrenheit","kelvin"],
    "Area": ["square_meter", "square_kilometer", "square_centimeter", "square_millimeter"],
    "Volume": ["cubic_meter", "cubic_centimeter"],
    "Speed": ["meter_per_second", "kilometer_per_hour"],
    "Time": ["second", "minute", "hour", "day"],
    "Digital Storage": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"]

}
category =st.selectbox("Select Category",list(categories.keys()))
value=st.number_input("Enter Value",format="%.2f")
col1,col2=st.columns(2)
with col1:
    from_unit=st.selectbox("Convert From",categories[category])
with col2:
    to_unit=st.selectbox("To",categories[category])
if st.button("Convert"):
    try:
        result=value*ureg(from_unit).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")
    except Exception as err:
        st.error(f"Conversion Error :{err}")