from streamlit.testing.v1 import AppTest

at = AppTest.from_file("testing_streamlit.py").run()

# Simulate the user incrementing the first number input three times
at.number_input[0].increment().run()
at.number_input[0].increment().run()
at.number_input[0].increment().run()

# Simulate the user incrementing the first number input one time
at.number_input[1].increment().run()

# Simulate the user clicking the "Add" button
at.button[0].click().run()
assert at.markdown[0].value == "The result is 4"