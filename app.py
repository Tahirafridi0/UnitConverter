import streamlit as st
import pandas as pd

st.title('Unit Converter')

# Create a sidebar for conversion type selection
conversion_type = st.sidebar.selectbox(
    'Select Conversion Type',
    ['Length', 'Weight', 'Temperature']
)

# Main content
st.header(f'{conversion_type} Converter')

# Input value
input_value = st.number_input('Enter value to convert:', value=0.0)

if conversion_type == 'Length':
    # Length conversion
    units = ['Meters', 'Kilometers', 'Miles', 'Feet', 'Inches']
    from_unit = st.selectbox('From:', units)
    to_unit = st.selectbox('To:', units)
    
    # Conversion logic
    if st.button('Convert'):
        # Convert everything to meters first
        meters = {
            'Meters': input_value,
            'Kilometers': input_value * 1000,
            'Miles': input_value * 1609.34,
            'Feet': input_value * 0.3048,
            'Inches': input_value * 0.0254
        }[from_unit]
        
        # Convert from meters to target unit
        result = {
            'Meters': meters,
            'Kilometers': meters / 1000,
            'Miles': meters / 1609.34,
            'Feet': meters / 0.3048,
            'Inches': meters / 0.0254
        }[to_unit]
        
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

elif conversion_type == 'Weight':
    # Weight conversion
    units = ['Kilograms', 'Grams', 'Pounds', 'Ounces']
    from_unit = st.selectbox('From:', units)
    to_unit = st.selectbox('To:', units)
    
    if st.button('Convert'):
        # Convert everything to kilograms first
        kg = {
            'Kilograms': input_value,
            'Grams': input_value / 1000,
            'Pounds': input_value * 0.453592,
            'Ounces': input_value * 0.0283495
        }[from_unit]
        
        # Convert from kg to target unit
        result = {
            'Kilograms': kg,
            'Grams': kg * 1000,
            'Pounds': kg / 0.453592,
            'Ounces': kg / 0.0283495
        }[to_unit]
        
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

else:
    # Temperature conversion
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
    from_unit = st.selectbox('From:', units)
    to_unit = st.selectbox('To:', units)
    
    if st.button('Convert'):
        # Convert to Celsius first
        celsius = {
            'Celsius': input_value,
            'Fahrenheit': (input_value - 32) * 5/9,
            'Kelvin': input_value - 273.15
        }[from_unit]
        
        # Convert from Celsius to target unit
        result = {
            'Celsius': celsius,
            'Fahrenheit': (celsius * 9/5) + 32,
            'Kelvin': celsius + 273.15
        }[to_unit]
        
        st.success(f'{input_value} {from_unit} = {result:.4f} {to_unit}')

# Add some information about the app
st.sidebar.markdown('---')
st.sidebar.info('This is a simple unit converter that supports length, weight, and temperature conversions.')
