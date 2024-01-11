import streamlit as st
from src.pipeline.prediction_pipeline import PredictPipeline,CustomData


def main():
    st.title("Diamond Price Prediction")
    # Create input boxes
    carat = st.number_input("carat", key="carat")
    depth = st.number_input("depth", key="depth")
    table = st.number_input("table", key="table")
    x = st.number_input("x", key="x")
    y = st.number_input("y", key="y")
    z = st.number_input("z", key="z")
    # Categorical data input
    cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
    cut = st.selectbox("cut", cut_categories, key="cut")
    color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
    color = st.selectbox("color", color_categories, key="color")
    clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
    clarity = st.selectbox("Clarity", clarity_categories, key="clarity")
    

    # Create submit button
    if st.button("Submit"):
        # Process input values and display results
        result = process_inputs(carat,depth,table,x,y,z, cut,color,clarity)
        st.success(f"Price will be : {result}")

def process_inputs(carat,depth,table,x,y,z, cut,color,clarity):
    data = CustomData(carat,depth,table,x,y,z, cut,color,clarity)
    final_data  = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(final_data)

    result = round(pred[0],2)

    return result

if __name__ == "__main__":
    main()
