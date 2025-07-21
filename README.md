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
graph TD
    A[Web Browser] --> B[Flask Application]
    B --> C[Authentication System]
    B --> D[Database Models]
    B --> E[Report Generation]
    C --> F[User Login/Logout]
    C --> G[Registration]
    C --> H[Password Hashing]
    D --> I[Technical Installation]
    D --> J[Exhaust Inspection]
    D --> K[Plant Inspection]
    D --> L[Certificate Models]
    E --> M[Word Export]
    E --> N[Excel Export]
    E --> O[PDF Export]
    B --> P[Activity Logging]
    B --> Q[File Upload Handling]
```

# Warehouse-Production-Tracking

``` mermaid
erDiagram
    USER ||--o{ USER_ACTIVITY : has
    USER {
        int id PK
        string username
        string email
        string password_hash
        string profile_picture
    }
    
    USER_ACTIVITY {
        int id PK
        int user_id FK
        string activity_type
        string description
        string ip_address
        string user_agent
        datetime created_at
    }
    
    PLANT_INSPECTION ||--o{ FUEL_SYSTEM : has
    PLANT_INSPECTION ||--o{ LUBE_SYSTEM : has
    PLANT_INSPECTION ||--o{ AIR_FILTRATION : has
    
    PLANT_INSPECTION {
        int PlantInspectionID PK
        string CustomerName
        string CustomerSite
        string Date
        string Time
        binary PhotoOfEquipmentInspected
    }
    
    FUEL_SYSTEM {
        int id PK
        int InspectionID FK
        string PrimaryFuelFilterPartNumber
        binary PrimaryFuelFilterPhoto
    }
    
    LUBE_SYSTEM {
        int id PK
        int InspectionID FK
        string OilFilterPartNumber
        binary OilFilterPhoto
    }
    
    AIR_FILTRATION {
        int id PK
        int InspectionID FK
        string AirCleanerModel
        binary AirCleanerArrangementPhoto
    }
```

# Warehouse-Production-Tracking

``` mermaid
sequenceDiagram
    participant User
    participant Browser
    participant Flask
    participant Database
    
    User->>Browser: Enters credentials
    Browser->>Flask: POST /login
    Flask->>Database: Query user by username
    Database-->>Flask: User record
    alt Valid credentials
        Flask->>Flask: Create session
        Flask->>Database: Log activity
        Flask-->>Browser: Redirect to dashboard
    else Invalid credentials
        Flask-->>Browser: Show error message
    end
```

# Warehouse-Production-Tracking

``` mermaid
flowchart TD
    A[Start] --> B{Report Type?}
    B -->|Word| C[Create Document]
    B -->|Excel| D[Create DataFrame]
    B -->|PDF| E[Create PDF Template]
    C --> F[Add Tables/Content]
    D --> G[Format Spreadsheet]
    E --> H[Build PDF Elements]
    F --> I[Save to Buffer]
    G --> I
    H --> I
    I --> J[Send File to User]
    J --> K[End]
```

# Warehouse-Production-Tracking

``` mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> FileSelected: User selects file
    FileSelected --> Validation: Submit
    Validation --> ValidFile: Extension allowed
    Validation --> InvalidFile: Extension not allowed
    ValidFile --> Processing: Save to uploads folder
    Processing --> DatabaseUpdate: Store filename
    DatabaseUpdate --> Success
    InvalidFile --> Error: Show message
    Success --> [*]
    Error --> [*]
```

# Warehouse-Production-Tracking

``` mermaid
gantt
    title Activity Logging Timeline
    dateFormat  YYYY-MM-DD HH:mm
    section User Session
    Login           :a1, 2023-01-01 09:00, 5m
    Page Views      :a2, after a1, 30m
    Form Submission :a3, after a2, 10m
    Logout          :a4, after a3, 2m
    
    section System
    DB Log Entry    :crit, 2023-01-01 09:00, 1m
    DB Log Entry    :crit, after a2, 1m
    DB Log Entry    :crit, after a3, 1m
```

# Warehouse-Production-Tracking

``` mermaid
journey
    title User Management Process
    section Admin
      Create User: 5: Admin
      Edit User: 3: Admin
      View Logs: 4: Admin
    section User
      Register: 5: User
      Login: 5: User
      Update Profile: 4: User
    section System
      Hash Password: 5: System
      Verify Credentials: 5: System
      Log Activity: 5: System
```

# Warehouse-Production-Tracking

``` mermaid
graph TD
    A[User] -->|HTTP Requests| B[Flask Application]
    B --> C[(MariaDB Database)]
    B --> D[Report Generation]
    B --> E[File Storage]
    C --> F[User Management]
    C --> G[Technical Installations]
    C --> H[Exhaust Inspections]
    C --> I[Plant Inspections]
    C --> J[Certificates]
    D --> K[Word/Excel/PDF]
    E --> L[Uploaded Images]
    F --> M[Authentication]
    F --> N[Activity Logging]
```

# Warehouse-Production-Tracking

``` mermaid
graph TD
    A[DoForms System] --> B1[User Management]
    A --> B2[Form Management]
    A --> B3[Reporting]
    A --> B4[Administration]
    
    B1 --> C1[Registration]
    B1 --> C2[Authentication]
    B1 --> C3[Profile Management]
    
    B2 --> C4[Technical Installation]
    B2 --> C5[Exhaust Inspection]
    B2 --> C6[Plant Inspection]
    B2 --> C7[Certificate Generation]
    
    B3 --> C8[Word Reports]
    B3 --> C9[Excel Export]
    B3 --> C10[PDF Generation]
    
    B4 --> C11[Activity Logs]
    B4 --> C12[System Monitoring]
    
    C4 --> D1[Equipment Data]
    C4 --> D2[Installation Photos]
    C4 --> D3[Warranty Tracking]
    
    C6 --> D4[Fuel System]
    C6 --> D5[Lube System]
    C6 --> D6[Air Filtration]
    C6 --> D7[12+ Subsystems]
```

# Warehouse-Production-Tracking

``` mermaid
flowchart TB
    subgraph UserJourney
        A[Login] --> B[Select Form Type]
        B --> C{Type?}
        C -->|Technical| D[Fill Installation Data]
        C -->|Exhaust| E[Complete Inspection]
        C -->|Plant| F[Detailed Equipment Check]
        D --> G[Upload Photos]
        E --> G
        F --> G
        G --> H[Submit Form]
        H --> I[Generate Report]
        I --> J[Email/Save]
    end
    
    subgraph SystemProcess
        H --> K[DB Persistence]
        I --> L[Report Rendering]
        K --> M[Data Validation]
        L --> N[Format Conversion]
        M --> O[Activity Log]
    end
```

# Warehouse-Production-Tracking

``` mermaid
graph LR
    U[User] -->|Form Data| W[Web Interface]
    W -->|POST Requests| A[Flask App]
    A -->|CRUD Operations| D[(Database)]
    A -->|File Storage| F[File System]
    D -->|Query Results| A
    A -->|Render| T[Templates]
    T -->|HTML| W
    A -->|Generate| R[Reports]
    R -->|PDF/Word/Excel| W
    F -->|Images| T
    A -->|Log| L[Activity DB]
```
