from app import app


"""
Home Page

Purpose: 
    Landing page introducing SeedSense with options to sign up or log in.

Components:
    Navigation Bar: Links to Sign Up & Login
    Introduction Text: Project overview
    Call to Action: Sign Up / Log In options

Links:
    Sign Up Page
    Login Page
"""
@app.route('/home', methods=['GET', 'POST'])
def Home():

    return render_template("index.html")



"""
Register Page

Purpose: 
    Create a new user account.

Components:
    Form Fields: Name, Email, Password (confirm password)
    Submit Button: Submit the form
    Validation: Ensure correct email format, password strength
    Success Message: Link to Login Page on success

Error Message: 
    Display if email already in use

Links:
    Login Page

"""
@app.route('/register', methods=['GET', 'POST'])
def Register():

    return


"""
Login Page

Purpose:
    Allow users to log in with their credentials.

Components:
    Form Fields: Email, Password
    Submit Button: Attempt login
    Remember Me: Option to stay logged in
    Error Message: Display if login fails
    Forgot Password: Link to reset password

Links:
    Schedule Dashboard
    Sign Up Page

"""
@app.route('/LogIn', methods=['GET', 'POST'])
def LogIn():

    return


"""
Logout Page

Purpose: 
    Log the user out and redirect.

Components:
    Confirmation: Confirm logout action
    Session End: Clear session data

Links:
    Home Page (or Login Page)

"""
@app.route('/LogOut', methods=['GET', 'POST'])
def LogOut():

    return


"""
Settings Page

Purpose:
    Configure account settings and preferences.

Components:
    
    Account Settings: Allow users to update their email address, password, and other personal info.
    Notification Preferences: Users can set the frequency of reminders for watering, crop growth stages, and more.
    Other Preferences: Configure preferences for seed input format, weather notifications, and any other customization.

Links:
    Schedule Dashboard
"""
@app.route('/Settings', methods=['GET', 'POST'])
def Settings():
    # The logic for managing user account settings and preferences will go here
    
    return render_template('settings.html')  # Example of rendering the page



"""
Seed Input Page

Purpose: 
    Input seed data like type, temperature, and watering requirements.

Components:
    Form Fields: Seed type, soil pH, temperature, light, watering schedule
    Submit Button: Save input
    Validation: Ensure all fields are filled and valid
    Confirmation: Message after successful input

Links:
    Schedule Dashboard
    Seed Location Page
    Crop Cycle Page

"""
@app.route('/SeedTypes', methods=['GET', 'POST'])
def SeedTypes():

    return


"""
Seed Location Page

Purpose:
    Input locations for seed planting through an interactive grid.

Components:

    Grid: Users select specific cells to assign seeds.
    Grid Size Input: Allows users to specify the size of the planting grid.
    Seed Selection: Users can choose the seed type to be planted in each selected grid cell.
    Confirm Button: Confirms the placement of the selected seeds on the grid.

Links:
    Schedule Dashboard
    Seed Input Page
    Crop Cycle Page
    Seed Plot Page 
"""
@app.route('/SeedLocation', methods=['GET', 'POST'])
def SeedLocation():

    return


"""
Seed Plot Page

Purpose:
    Display and visualize the grid with the planted seeds.

Components:

    Grid Display: A visual representation of the grid with planted seeds.
    Seed Info: Display details for each seed in the grid (e.g., seed type, planting date).
    Edit Button: Allows users to modify seed placements or grid configurations.
    Confirm Button: Confirms any changes made to the seed plot.
    
Links:
    Schedule Dashboard
    Seed Location Page
    Seed Input Page
    Crop Cycle Page
"""
@app.route('/SeedPlot', methods=['GET', 'POST'])
def SeedPlot():
    
    return 


"""
Schedule Dashboard Page

Purpose: 
    Central hub to manage seed schedules, settings, and more.

Components:
    Overview: Summary of schedules, progress, upcoming events
    Navigation: Links to Settings, Seed Input, Seed Distribution, Crop Cycle, Logout
    Status Indicators: Reminders for watering, deadlines
    Calendar/Timeline: View and manage seed growth timeline

Links:
    Settings Page
    Seed Input Page
    Seed Distribution Page
    Crop Cycle Page
    Crop Cycle Reccomend Page
    Logout

"""
@app.route('/SchedBoard', methods=['GET', 'POST'])
def ScheduleDashboard():

    return


"""
Crop Cycle Page

Purpose:
    User defines the timeperiod of the crop cycle

Components:
    


Links:
    Schedule Dashboard
    Seed Input Page
    Seed Distribution Page
    Crop Cycle Reccomend Page
"""
@app.route('/CropCycle', methods=['GET', 'POST'])
def CropCycle():

    
    return 


"""
Crop Cycle Reccomend Page

Purpose:
    System reccomends the next cycle based on the previous one

Components:
    


Links:
    Schedule Dashboard
    Seed Input Page
    Seed Distribution Page
"""
@app.route('/RecCycle', methods=['GET', 'POST'])
def RecCycle():

    
    return 
