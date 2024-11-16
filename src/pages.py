import index, dashboard

homePage = st.Page(index.Index(), url_path="/", title="Home")
dashboardPage = st.Page(dashboard.Dashboard(), url_path="/dashboard", title="Dashboard")

pages = [
    homePage,
    dashboardPage
]
