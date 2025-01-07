
# Ticketing System

## Project Overview  
The **Ticketing System** is a robust backend infrastructure designed to support an event ticket marketplace. Users can list tickets for sale (concerts, sports events), purchase tickets, and manage orders seamlessly. The system ensures scalability, fault tolerance, and secure communication between services.  

### Key Features:  
- **Microservices Architecture**: Independent services for user authentication, ticket management, order processing, payment handling, and expiration management.  
- **Asynchronous Communication**: Uses **RabbitMQ** for event-driven communication between services.  
- **Scalability and Deployment**: Built with **Kubernetes** and **Docker**, enabling efficient scaling and seamless deployment.  
- **Secure Payments**: Integrates with **Stripe** for secure credit card payments.  
- **JWT Authentication**: Ensures secure user authentication across services.  

---

## Technologies Used  
### Backend Infrastructure  
- **Kubernetes**: For container orchestration and managing service scaling.  
- **Docker**: For containerizing services, ensuring consistent and portable environments.  
- **RabbitMQ**: For handling asynchronous events in a decoupled system.  
- **Flask**: Lightweight and fast web framework for APIs.  
- **Redis**: Used for caching and handling expiration events.  

### Security  
- **JWT (JSON Web Tokens)**: Secure user authentication and session management.  
- **Secure Communication**: Services interact securely with clearly defined API boundaries.  

### Database  
- **MongoDB**: NoSQL database for storing tickets, orders, and user data.  

---

## Microservices Overview  
### 1. **Auth Service**  
- Handles user signup, login, and logout.  
- Routes:  
  - `POST /api/users/signup`  
  - `POST /api/users/signin`  
  - `POST /api/users/signout`  
  - `GET /api/users/currentuser`  

### 2. **Tickets Service**  
- Manages ticket creation, updates, and validation.  

### 3. **Orders Service**  
- Manages order creation, editing, and tracking status (Created, Cancelled, Awaiting Payment, Completed).  

### 4. **Expiration Service**  
- Monitors pending orders and cancels them if not paid within 15 minutes.  

### 5. **Payments Service**  
- Handles credit card payments via **Stripe**.  
- Cancels orders if payment fails or completes them upon success.  

---

## Event Flow and Communication  
### Events Used:
- `UserCreated`, `UserUpdated`  
- `TicketCreated`, `TicketUpdated`  
- `OrderCreated`, `OrderCancelled`, `OrderExpired`  
- `ChargeCreated`  

Each service publishes and subscribes to relevant events via RabbitMQ for decoupled and efficient communication.  

---

## System Design Highlights  
### Scalability  
- Services are independently scalable using Kubernetes.  
- Horizontal pod autoscaling for handling high traffic.  

### Fault Tolerance  
- Each service operates independently to ensure system reliability.  
- RabbitMQ ensures message delivery even during service downtimes.  

### Development Challenges Addressed  
- Code duplication minimized with a shared **common library**.  
- Event properties standardized for easier testing and debugging.  

---

## Deployment  
The system is deployed on a **Kubernetes cluster** with the following workflow:  
1. Build Docker images for each service.  
2. Deploy services to the cluster using Kubernetes manifests.  
3. Use **NGINX Ingress** for routing traffic to appropriate services.  

---

## Future Enhancements  
- Implement AI-based recommendations for ticket purchases.  
- Add analytics for user behavior and ticket sales.  
- Introduce feature-based service design for more complex business logic.  

---

## Getting Started  
### Prerequisites  
- Docker and Kubernetes installed.  
- Access to a Kubernetes cluster.  
- MongoDB and RabbitMQ configured.  

### Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/madhurachanna/ticketing  
   cd ticketing  
   ```  
2. Build and run Docker containers:  
   ```bash  
   docker-compose up --build  
   ```  
3. Deploy to Kubernetes:  
   ```bash  
   kubectl apply -f k8s/  
   ```  

---

## Authors  
**Madhurachanna H B**  

---  

## License  
This project is licensed under the MIT License.  
