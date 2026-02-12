## 📋 Features

- ✅ Complete CRUD operations (Create, Read, Update, Delete)
- ✅ RESTful API design with GET, POST, PUT, DELETE methods
- ✅ SQLite database for data persistence
- ✅ Input validation and error handling
- ✅ Docker containerization for consistent deployment
- ✅ GitHub Actions CI/CD pipeline for automated testing and deployment
- ✅ Security best practices (parameterized queries to prevent SQL injection)

## 🏗️ Architecture

The API follows a three-layer architecture:

- **Layer A (Database):** SQLite database operations
- **Layer B (Business Logic):** Data validation and transformation
- **Layer C (API):** HTTP endpoints and request handling

## 🔧 Tech Stack

- **Language:** Python 3.9
- **Framework:** Flask 2.3.0
- **Database:** SQLite3
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Deployment:** Railway.app (not anymore)

## 📦 Project Structure

```
ecommerce-api/
├── app.py                 # Main Flask application
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── ecommerce.db         # SQLite database
├── .github/
│   └── workflows/
│       └── deploy.yml   # CI/CD pipeline configuration
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker (optional, for containerization)
- Git

### Local Development

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR-USERNAME/ecommerce-api.git
cd ecommerce-api
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python app.py
```

4. **Test the API:**
```bash
# GET all products
curl http://127.0.0.1:5000/products

# POST a new product
curl -X POST http://127.0.0.1:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Laptop","price":1000,"stock":5,"category":"Electronics"}'
```

### With Docker

1. **Build the Docker image:**
```bash
docker build -t ecommerce-api .
```

2. **Run the container:**
```bash
docker run -p 5000:5000 ecommerce-api
```

3. **Access the API:**
```
http://127.0.0.1:5000/
```

## 📚 API Endpoints

### GET /
Returns welcome message.

### GET /products
Returns all products in the database.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 1000,
    "stock": 5,
    "category": "Electronics"
  }
]
```

### POST /products
Create a new product.

**Request Body:**
```json
{
  "name": "Mouse",
  "price": 50,
  "stock": 20,
  "category": "Accessories"
}
```

**Response:**
```json
{
  "message": "Product added successfully"
}
```

### PUT /products/<id>
Update an existing product.

**Request Body:**
```json
{
  "name": "Updated Laptop",
  "price": 1200,
  "stock": 3,
  "category": "Electronics"
}
```

### DELETE /products/<id>
Delete a product.

**Response:**
```json
{
  "message": "Product deleted successfully"
}
```

## 🔄 CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment:

1. **Trigger:** On every push to the `main` branch
2. **Build:** Docker image is built and tested
3. **Test:** Python dependencies are verified
4. **Deploy:** Automatically deployed to Railway.app

View pipeline status: `Actions` tab on GitHub

## 🛡️ Security Features

- **SQL Injection Prevention:** Uses parameterized queries
- **Input Validation:** Validates required fields before processing
- **Error Handling:** Proper error responses without exposing sensitive information

## 📈 Future Improvements

- Add async/await for better concurrency handling
- Migrate to PostgreSQL for production reliability
- Implement user authentication and authorization
- Add comprehensive unit and integration tests
- Implement rate limiting for API endpoints
- Add API documentation with Swagger/OpenAPI

## 🧠 Key Learning Outcomes

This project demonstrates:
- ✅ RESTful API design principles
- ✅ CRUD operations implementation
- ✅ Database design and SQL queries
- ✅ Docker containerization
- ✅ CI/CD pipeline automation
- ✅ Security best practices
- ✅ Three-layer architecture pattern
- ✅ Error handling and validation

## 📖 How to Use This as a Portfolio Project

1. **Share the live link:** Send employers the Railway URL
2. **Show your code:** Point to this GitHub repository
3. **Explain the architecture:** Walk them through the three layers
4. **Discuss deployment:** Explain Docker and CI/CD pipeline
5. **Demonstrate security:** Discuss SQL injection prevention and input validation

## 🤝 Contributing

Feel free to fork this project and add your own features!

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built as a learning project to demonstrate full-stack development skills.
