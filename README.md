# Warehouse-Production-Tracking

``` mermaid
graph LR
    %% System Components
    A[Web Portal] -->|HTTP Requests| B[Flask API]
    B -->|CRUD Operations| C[(PostgreSQL/SQLite)]
    C -->|Data Persistence| B
    B -->|JSON Responses| A
    
    %% Sub-components
    subgraph Web Portal
        A1[Dashboard]
        A2[Task Management]
        A3[Employee Management]
    end
    
    subgraph Flask API
        B1[Authentication]
        B2[Task Routes]
        B3[Employee Routes]
        B4[Reporting Endpoints]
    end
    
    subgraph Database
        C1[Employees Table]
        C2[Tasks Table]
    end
    
    %% Critical Dependencies
    A1 -->|Relies on| B4
    A2 -->|Depends on| B2
    A3 -->|Requires| B3
    B2 -->|Reads/Writes| C2
    B3 -->|Manages| C1
    B1 -->|Secures| B2
    B1 -->|Secures| B3
    B1 -->|Secures| B4
    
    %% External Dependencies
    B -->|Email Alerts| D[SMTP Server]
    B -->|File Storage| E[Cloud Storage]
```

# Warehouse-Production-Tracking

``` mermaid
graph LR
    User-->|Login|Auth-->|JWT|API-->|Session|DB
    Manager-->|Create Task|API-->|INSERT|DB
    Worker-->|Update Status|API-->|UPDATE|DB
    System-->|Scheduled Reports|API-->|Aggregate|DB
```

# Warehouse-Production-Tracking

``` mermaid
graph TD
    F1[API Server] -->|Backup| F2[Load Balancer]
    F3[Primary DB] -->|Replica| F4[Standby DB]
    F5[SMTP] -->|Fallback| F6[SMS Gateway]
```

# Warehouse-Production-Tracking

``` mermaid
sequenceDiagram
    participant MobileApp
    participant Backend
    participant Database
    participant WebPortal

    MobileApp->>Backend: POST /login (Credentials)
    Backend->>Database: SELECT user
    Database-->>Backend: User Data
    Backend-->>MobileApp: JWT Token

    WebPortal->>Backend: GET /analytics
    Backend->>Database: Aggregate Data
    Database-->>Backend: Results
    Backend-->>WebPortal: Dashboard HTML
```

# Warehouse-Production-Tracking

``` mermaid
erDiagram
    USER ||--o{ ORDER : "places"
    USER {
        int id PK
        string name
        string email
    }
    ORDER {
        int id PK
        int user_id FK
        date created_at
    }
```

# Warehouse-Production-Tracking

``` mermaid
classDiagram
    class UserController {
        +login()
        +logout()
    }
    class DatabaseService {
        +query()
        +update()
    }
    UserController --> DatabaseService : "Uses"
```

# Warehouse-Production-Tracking

``` mermaid
stateDiagram-v2
    [*] --> SplashScreen
    SplashScreen --> Login
    Login --> Home: Success
    Login --> Error: Failed
    Home --> Settings
    Home --> Logout
    Logout --> Login
```


# Warehouse-Production-Tracking

``` mermaid
flowchart TD
    A[Mobile App] -->|API Call| B[Backend]
    B -->|SQL Query| C[(Database)]
```


# Warehouse-Production-Tracking

``` mermaid
erDiagram
    CUSTOMER ||--o{ TICKET : "has"
    COUNTER ||--o{ TICKET : "processes"
    TICKET }|--|| COUNTER : "assigned to"

    CUSTOMER {
        integer id PK
        varchar(100) name
        varchar(20) phone
        integer ticket_id FK
    }

    TICKET {
        integer id PK
        varchar(20) number UK
        varchar(20) status
        datetime created_at
        datetime called_at
        datetime completed_at
        integer counter_id FK
        boolean unsuccessful
        varchar(100) reason
    }

    COUNTER {
        integer id PK
        varchar(50) name
        boolean is_active
        integer current_ticket_id FK
    }
```

# Warehouse-Production-Tracking

``` mermaid
classDiagram
    class Customer {
        +id: integer (PK)
        +name: varchar(100)
        +phone: varchar(20)
        +ticket_id: integer (FK)
    }

    class Ticket {
        +id: integer (PK)
        +number: varchar(20) (UQ)
        +status: varchar(20)
        +created_at: datetime
        +called_at: datetime
        +completed_at: datetime
        +counter_id: integer (FK)
        +unsuccessful: boolean
        +reason: varchar(100)
    }

    class Counter {
        +id: integer (PK)
        +name: varchar(50)
        +is_active: boolean
        +current_ticket_id: integer (FK)
    }

    Customer "1" --> "1" Ticket : has
    Counter "1" --> "0..1" Ticket : processes
    Ticket "0..1" --> "1" Counter : assigned to
```


# Warehouse-Production-Tracking

``` mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> TicketCreation: "Create Ticket"
    TicketCreation --> TicketCreated: "Submit"
    TicketCreated --> Waiting: "Queue"
    
    state Waiting {
        [*] --> InQueue
        InQueue --> Called: "Counter calls"
        Called --> Serving
        Serving --> Completed: "Service finished"
        Serving --> Unsuccessful: "Service failed"
    }
    
    Completed --> [*]
    Unsuccessful --> [*]
    TicketCreated --> [*]: "Cancel"
```

# Warehouse-Production-Tracking

``` mermaid
sequenceDiagram
    participant MobileApp
    participant API
    participant Database
    
    MobileApp->>API: POST /tickets (create new ticket)
    API->>Database: INSERT ticket
    Database-->>API: New ticket ID
    API-->>MobileApp: Ticket details (with number)
    
    MobileApp->>API: GET /tickets/{number} (poll status)
    alt Ticket not called
        API-->>MobileApp: "In Queue"
    else Ticket called
        API->>Database: UPDATE ticket status
        API-->>MobileApp: "Called - Counter 3"
    end
    
    CounterSystem->>API: PUT /counters/{id}/current_ticket
    API->>Database: UPDATE counter and ticket
```


# Warehouse-Production-Tracking

``` mermaid
gantt
    title Ticket System Development Timeline
    dateFormat  YYYY-MM-DD
    section Core
    Database Design       :done,    db1, 2024-01-01, 7d
    API Development      :active,  api1, 2024-01-08, 14d
    Mobile App UI        :         ui1, 2024-01-22, 21d
    section Counter System
    Counter Hardware     :         hard1, 2024-01-15, 14d
    Counter Software     :         soft1, 2024-01-29, 14d
    section Testing
    Unit Tests           :         test1, 2024-02-12, 7d
    Integration Testing  :         test2, 2024-02-19, 7d
```

# Warehouse-Production-Tracking

``` mermaid
flowchart TD
    A[Start] --> B{Customer Action}
    B -->|New Ticket| C[Generate Ticket Number]
    C --> D[Save to Database]
    D --> E[Display Ticket Info]
    
    B -->|Check Status| F[Query Ticket]
    F --> G{Status?}
    G -->|In Queue| H[Show Position]
    G -->|Called| I[Display Counter]
    G -->|Completed| J[Show Feedback]
    
    K[Counter Interface] --> L{Next Ticket}
    L --> M[Call Next in Queue]
    M --> N[Update Status]
    N --> O[Display Current Ticket]
```

# Warehouse-Production-Tracking

``` mermaid
stateDiagram-v2
    [*] --> Ready
    Ready --> Calling: "Call next ticket"
    Calling --> Serving: "Customer arrives"
    Serving --> Completed: "Finish service"
    Serving --> Unsuccessful: "Customer missing"
    Completed --> Ready
    Unsuccessful --> Ready
```

# Warehouse-Production-Tracking

``` mermaid
flowchart LR
    Created --> Queued
    Queued --> Called
    Called --> Served
    Called --> Missed
    Served --> Completed
    Missed --> Requeued
    Requeued --> Called
```

# Warehouse-Production-Tracking

``` mermaid

```

# Warehouse-Production-Tracking

``` mermaid
```
