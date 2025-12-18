<!-- mermaid rules -->

## Padrões para Diagramas Mermaid

### Sintaxe Básica

Use blocos de código com a linguagem `mermaid`:

````markdown
```mermaid
graph TD
    A[Início] --> B[Processo]
    B --> C[Fim]
```
````

### Tipos de Diagramas

#### Flowchart (Fluxograma)

```mermaid
graph TD
    A[Start] --> B{Decisão}
    B -->|Sim| C[Ação 1]
    B -->|Não| D[Ação 2]
    C --> E[End]
    D --> E
```

#### Sequence Diagram (Sequência)

```mermaid
sequenceDiagram
    participant U as User
    participant A as API
    participant D as Database
    U->>A: Request
    A->>D: Query
    D-->>A: Response
    A-->>U: Data
```

#### Class Diagram (Classes)

```mermaid
classDiagram
    class User {
        +String name
        +String email
        +login()
        +logout()
    }
```

#### State Diagram (Estados)

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : start
    Processing --> Done : complete
    Done --> [*]
```

#### ER Diagram (Entidades)

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ITEM : contains
```

### Boas Práticas

- **Direção**: Use `TD` (top-down) ou `LR` (left-right)
- **Nomes**: Use identificadores curtos (A, B, C) com labels descritivos
- **Cores**: Use classes CSS para destacar elementos importantes
- **Simplicidade**: Mantenha diagramas focados em um conceito

### Estilos Customizados

```mermaid
graph TD
    A[Normal]:::default --> B[Destaque]:::highlight
    classDef default fill:#f9f9f9,stroke:#333
    classDef highlight fill:#ff6b6b,stroke:#333,color:#fff
```

### Preview no VS Code/Cursor

Instale a extensão:

- **Markdown Preview Mermaid Support** (`bierner.markdown-mermaid`)

Ou use o preview nativo do GitHub (push e visualize no repo).

