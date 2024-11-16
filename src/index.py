import streamlit as st

import common

common.header()

st.title("Pump & Dump Partners")
st.subheader("An investment advice bureau that starts with you.")
st.subheader("The most trustworthy investment advice bureau in the world.")

st.header("Ready to Invest?")
st.page_link("dashboard.py", label="Get Started")

st.header("Our Top Picks for Today")
c1, c2, c3 = st.columns(3)
c1.metric("Doge", "100", "-4102")
c2.metric("JeffCoin", "200", "-13002")
c3.metric("Hello Coin", "-1023", "-99920")

st.header("Our Values")
st.write("At Pump & Dump Partners, we believe that every investment should start and end with you.")

st.header("Our Reviews")
st.write("We always deliver at Pump & Dump Partners, that's why we have hundreds of positive comments about our sevices.")
st.write("But don't let us tell you, have a look for yourself!")
st.markdown('''
> I invested my life savings in JeffCoin and now I'm broke. Thanks Pump & Dump Partners!
>
> *Karen, 69*

> I invested my life savings in Doge and now I'm broke. Thanks Pump & Dump Partners!
>
> *John, 42*

> I invested my life savings in Hello Coin and now I'm broke. Thanks Pump & Dump Partners!
>
> *Jane, 35*
''')

common.footer()
