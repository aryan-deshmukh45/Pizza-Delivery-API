## Pizza Delivery API

A secure and scalable Pizza Delivery REST API built using FastAPI, PostgreSQL/SQLite, JWT Authentication, and Stripe Payment Integration.
This project demonstrates real-world backend development including authentication, order management, and payment processing.


## ROUTES TO IMPLEMENT

| METHOD | ROUTE                                   | FUNCTIONALITY                     | ACCESS        |
|--------|------------------------------------------|-----------------------------------|--------------|
| POST   | /auth/signup/                           | Register new user                | Public       |
| POST   | /auth/login/                            | Login user and get JWT token     | Public       |
| POST   | /orders/order/                          | Place a new pizza order          | Authenticated|
| GET    | /orders/                                | Test protected route             | Authenticated|
| GET    | /orders/user/orders/                    | Get current user's orders        | Authenticated|
| GET    | /orders/user/order/{id}/                | Get specific user order          | Authenticated|
| PUT    | /orders/order/update/{id}/              | Update order details             | Authenticated|
| PATCH  | /orders/order/update/{id}/              | Update order status              | Admin Only   |
| DELETE | /orders/order/delete/{id}/              | Delete an order                  | Authenticated|
| GET    | /orders/orders/                         | Get all orders                   | Admin Only   |
| POST   | /orders/payment/create/{order_id}/      | Create Stripe PaymentIntent      | Authenticated|
| GET    | /orders/payment/confirm/{order_id}/     | Confirm Stripe payment           | Authenticated|
| GET    | /docs                                   | Swagger API Documentation        | Public       |


## Application Workflow

### 1 User Registration
- User sends a `POST /auth/signup/` request.
- Password is hashed securely.
- User data is stored in the database.
---
### 2 User Login (JWT Authentication)
- User sends `POST /auth/login/` with credentials.
- Server verifies username and password.
- A JWT access token is generated.
- User must include this token in the `Authorization` header for protected routes.
Example:
Authorization: Bearer <access_token>
---
### 3 Place Order
- User sends `POST /orders/order/`
- JWT token is validated.
- Order details (pizza_size, quantity) are received.
- Total amount is calculated.
- Stripe PaymentIntent is created.
- Order is stored in the database with:
  - payment_status = "PENDING"
  - order_status = "CREATED"
- Backend returns Stripe `client_secret`.
---
### 4 Payment Processing (Stripe)
- Frontend uses `client_secret` to complete payment.
- Stripe securely processes card payment.
- If payment succeeds → PaymentIntent status becomes `succeeded`.
---
### 5 Payment Confirmation
- User calls `GET /orders/payment/confirm/{order_id}/`
- Backend retrieves Stripe PaymentIntent.
- If status is `succeeded`:
  - payment_status = "PAID"
  - order_status = "CONFIRMED"
- Database is updated.
---
### 6 Order Management

#### Normal User:
- View own orders
- Retrieve specific order
- Update order (if allowed)
- Delete own order

#### Admin (is_staff = True):
- View all orders
- Update order status (e.g., PREPARING, DELIVERED)
- Manage full order lifecycle
---
###  Security Flow
- Password hashing
- JWT-based authentication
- Role-based authorization
- Stripe secure PaymentIntent API
- Environment variables for secret keys
---
### Database Relationships
- One User → Many Orders
- Each Order → Belongs to one User
- Each Order → Linked to Stripe PaymentIntent ID