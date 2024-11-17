import streamlit as st
import database

st.title("Pump & Dump Partners")
st.subheader("An investment advice bureau that starts with you.")
st.subheader("The most trustworthy investment advice bureau in the world.")

st.header("Ready to Invest?")
st.page_link("dashboard.py", label="Get Started")

top_picks = (sorted(database.fetch_joined_coin_datapoints(), key=lambda x:float(x["24hr_change"]))[:3])

st.header("Our Top Picks for Today")
c1, c2, c3 = st.columns(3, gap="large")
c1.metric(top_picks[0]["name"], f"${top_picks[0]["datapoints"][-1]["value"]}", f"{float(top_picks[0]["24hr_change"]): .2f}%")
c2.metric(top_picks[1]["name"], f"${top_picks[1]["datapoints"][-1]["value"]}", f"{float(top_picks[1]["24hr_change"]): .2f}%")
c3.metric(top_picks[2]["name"], f"${top_picks[2]["datapoints"][-1]["value"]}", f"{float(top_picks[2]["24hr_change"]): .2f}%")


st.header("Our Values")
st.write("At Pump & Dump Partners, we strongly believe in buying the dip. Bearish means bullish in our eyes!")
st.write("Every day we grow towards a brighter future, and with you on board we will embark on a creative voyage.")
st.image("https://www.shutterstock.com/shutterstock/photos/102307264/display_1500/stock-photo-group-of-happy-people-isolated-over-white-background-102307264.jpg")

st.header("Our Reviews")
st.write("We always deliver at Pump & Dump Partners, that's why we have hundreds of positive comments about our sevices.")
st.write("But don't let us tell you, have a look for yourself!")

c1, c2 = st.columns([2, 1], vertical_alignment="center")

c1.markdown('''
> I invested my life savings in JeffCoin and now I'm broke. Thanks Pump & Dump Partners!
>
> *Karen, 69*
''')
c2.image("https://thumbs.dreamstime.com/z/portrait-beautiful-adult-happy-woman-thumbs-up-sign-over-white-background-31744174.jpg", width=100)

st.text("")

c1, c2 = st.columns([1, 2], vertical_alignment="center")

c1.image("https://thumbs.dreamstime.com/b/happy-man-okay-sign-portrait-white-background-showing-31416492.jpg", width=100)

c2.markdown('''
> I invested my life savings in Doge and now I'm broke. Thanks Pump & Dump Partners!
>
> *John, 42*
''')

st.text("")

c1, c2 = st.columns([2, 1], vertical_alignment="center")

c1.markdown('''
> I invested my life savings in Hello Coin and now I'm broke. Thanks Pump & Dump Partners!
>
> *Jane, 35*
''')

c2.image("https://media.istockphoto.com/id/1494508936/photo/happy-excited-and-phone-with-black-woman-in-studio-for-text-message-notification-and-social.jpg?s=612x612&w=0&k=20&c=9h-m2tus81J0dKxb81KEEXDy1Xoo84mZ7bjVGwDjEro=", width=100)
