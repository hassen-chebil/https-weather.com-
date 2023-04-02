import streamlit as st
import requests, json 



def main():

    st.markdown(
    """
    <style>
        .stApp {
            background-color: #78D5DA;
            color: black;
            font-size: 48px;
        }

        button {
            background-color: #FFFFFF !important;
            color: blue !important;
            border-radius: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


    st.title("Smart Weather Prediction")
    pays = st.text_input("Enter the city name:")
  
    # Enter your API key here 
    api_key = "b8e909c7c126a848d7d7ea55ceeeeaad"

    # base_url variable to store url 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # complete_url variable to store 
    # complete url address 
    complete_url = base_url + "appid=" + api_key + "&q=" + pays +"&units=metric"
    

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url) 

    # convert json format data into 
    # python format data 
    x = response.json() 

    # Now x contains list of nested dictionaries 
    # Check the value of "cod" key is equal to 
    # "404", means city is found otherwise, 
    # city is not found 

    if x["cod"] != "404": 

        # store the value of "main" 
        # key in variable y 
        y = x["main"] 

        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 

        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 

        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 

        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 

        # store the value corresponding 
        # to the "description" key at 
        # the 0th index of z 
        weather_description = z[0]["description"]
        
    



    if st.button("Display" ):
        col1, col2 = st.columns([6, 8])
        with col2:
            st.metric(label="Température",value=str(current_temperature) + "°C")
            st.metric(label="Atmospheric pressure",value=str(current_pressure) + " hPa")
            st.metric(label="Humidity",value=str(current_humidiy) + " %")
            st.metric(label="Description",value=str(weather_description) )
                
        with col1 :
            image = "weather-logo.png" # or a URL
            st.image(image, width=250)

if __name__ == "__main__":
    
    try:
        main()
    except:
            st.write("City not Found !")


