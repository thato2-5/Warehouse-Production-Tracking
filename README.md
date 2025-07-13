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
