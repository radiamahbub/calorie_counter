# 🥗 Calorie Tracker — Django Web Application

A web-based calorie tracking application built with **Python and Django** that helps users manage their profiles, record consumed calories, search food entries, and monitor their daily calorie intake against their Basal Metabolic Rate (BMR).

## ✨ Features

* **User Authentication** — Register, log in, and log out securely.
* **User Profiles** — Create and update personal profile information.
* **Calorie Tracking** — Add, view, update, and delete consumed-calorie records.
* **Search Functionality** — Search calorie records by food or item name.
* **Personalized Dashboard** — View BMR, total calories consumed, and remaining calories.
* **User-Specific Records** — Display calorie entries belonging to the logged-in user.
* **Form Validation** — Validate submitted data using Django forms.
* **Database Aggregation** — Calculate total calorie intake using Django ORM aggregation.
* **Responsive UI** — Built using Bootstrap-compatible form styling.

## 🛠️ Tech Stack

| Technology            | Purpose                          |
| --------------------- | -------------------------------- |
| Python                | Core programming language        |
| Django                | Web framework                    |
| SQLite                | Development database             |
| HTML5                 | Page structure                   |
| CSS3                  | Styling                          |
| Bootstrap             | Responsive UI components         |
| Django ORM            | Database queries and aggregation |
| Django Authentication | User registration and login      |

## 📸 Application Modules

### 1. Dashboard

Displays the user's BMR, total consumed calories, and remaining calories.

### 2. User Profile

Allows authenticated users to maintain their profile information.

### 3. Calorie Management

Users can add, view, edit, delete, and search their calorie records.

### 4. Authentication

Provides registration, login, and logout functionality.

## ⚙️ Installation and Setup

### Prerequisites

* Python installed
* pip package manager
* Git (optional)

### Step 1: Clone the repository

```bash
git clone https://github.com/radiamahbub/calorie-counter.git
cd calorie-tracker
```

Replace `YOUR_USERNAME` and the repository name with your actual GitHub details.

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Django

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install Django:

```bash
pip install django
```

### Step 4: Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your account.

### Step 6: Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

## 📂 Project Structure

The following is an illustrative structure based on the modules in your code. Adjust it to match your actual folders and files.

```text
calorie-tracker/
├── accounts/
│   ├── forms.py
│   ├── views.py
│   └── ...
├── tracker/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/
│   ├── form_base.html
│   └── tracker/
│       ├── dashboard.html
│       ├── profile.html
│       └── calorie_consume_list.html
├── manage.py
├── requirements.txt
└── README.md
```

## 🧮 Dashboard Calculation

The application calculates the remaining calories using:

**Remaining Calories = BMR − Total Consumed Calories**

The total calorie intake is calculated using Django's `Sum()` aggregation.

The dashboard also compares total consumed calories with BMR to determine which message to display.

*Note: BMR is an estimate of the calories the body uses at rest. It is not the same as total daily energy expenditure or a personalized daily calorie target.*

## 🔐 Security Notes

* Authentication is required for the dashboard and calorie-management views.
* Calorie records are filtered by the logged-in user in the listing and dashboard views.
* Before deploying publicly, ensure that update and delete operations verify record ownership, forms are protected against unauthorized changes, and production security settings are configured correctly.
* Never commit passwords, secret keys, or other sensitive configuration values to GitHub.

## 🚀 Future Improvements

* [ ] Food database with nutritional information
* [ ] Daily, weekly, and monthly calorie summaries
* [ ] Macronutrient tracking (protein, carbohydrates, and fat)
* [ ] Interactive charts and visual analytics
* [ ] Calorie goals and progress tracking
* [ ] REST API integration
* [ ] Automated testing
* [ ] Production deployment

## 🎯 Learning Objectives

This project provides practical experience with:

* Django function-based views
* Models, forms, and database relationships
* User authentication and authorization
* CRUD operations
* GET-based search functionality
* Django ORM filtering and aggregation
* Template rendering and redirects
* Git and GitHub project documentation

## 👩‍💻 Author

**Radia Mahbub**

Full-Stack Developer | Python & Django Learner

* GitHub: [@radiamahbub](https://github.com/radiamahbub)
* LinkedIn: [Radia Mahbub](https://www.linkedin.com/in/radiamahb/)

---

*Built as a hands-on project to strengthen Python and Django web development skills.*
