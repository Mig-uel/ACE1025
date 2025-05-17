# Software Engineering Full Stack Web Development (ACE1025)

The repo for QCC Software Engineering Micro-Credential Career Track in Web Development (Bootcamp)

## Project 2 - E-Commerce Website (Full-Stack Project)

This is my second project in a full-stack development bootcamp, where I built a fully functional **e-commerce web application** using both front-end and back-end technologies. The app simulates a real online shopping experience — from product browsing and cart management to user authentication and order confirmation.

---

## 🔧 Tech Stack

- **Front-End**: HTML, CSS *(or Bootstrap for styling and layout)*
- **Back-End**: Python with the Flask framework
- **Database**: PostgreSQL

---

## 💡 Features

### 🛍️ Product Catalog
- Includes **at least two categories** (e.g., *Electronics*, *Clothing*)
- Each category shows **at least six products**
- Each product displays:
  - Name
  - Image
  - Price
  - Quantity input
  - "Add to Cart" button

### 🛒 Shopping Cart
- Shows all items added by the user
- Users can:
  - Remove individual items
  - See the total cost (including tax and shipping/handling)
- Includes:
  - **Sign-Up** button for new customers
  - **Login** button for returning users

### 👤 User Registration & Login
- Registration form collects:
  - First Name, Last Name
  - Username, Password
  - Email, Address
- Checks for **duplicate usernames or emails**
- After registration, users are redirected to the **Login Page**
- Successful login redirects to the **Checkout Page**

### ✅ Checkout & Order Confirmation
- The Checkout Page shows:
  - Cart items
  - Total cost (with tax and shipping)
  - “Submit Order” button
- On submitting the order:
  - User is redirected to a **Completed Order** page
  - Displays a confirmation message with a **randomly generated Order Number**
  - Simulates that payment and shipping info were already provided

---

## 🗃️ Database Schema

### `users` Table
| Field       | Type        | Notes                     |
|-------------|-------------|---------------------------|
| id          | Primary Key | Auto-incrementing integer |
| first_name  | Text        |                           |
| last_name   | Text        |                           |
| username    | Text        | Unique                    |
| password    | Text        |                           |
| email       | Text        | Unique                    |
| address     | Text        |                           |

### `orders` Table
| Field       | Type        | Notes                                  |
|-------------|-------------|----------------------------------------|
| order_id    | Primary Key | Auto-incrementing integer              |
| user_id     | Foreign Key | References `users.id`                  |
| order_info  | JSON/Text   | Contains item details and total price |

---

## 🎯 Project Goals

The goal was to bring together the core building blocks of a full-stack application by:
- Creating an interactive, styled front-end
- Building secure and functional back-end routes
- Managing user sessions and validations
- Integrating a relational database
- Delivering a complete e-commerce flow

By completing this project, I now have a strong foundation for building and deploying dynamic, database-driven web applications.

---

## 📸 Screenshots

_(Screenshots of catalog page, cart page, registration form, and order confirmation coming soon!)_


