```mermaid
classDiagram

class Shape {
  - color
  + clone()
  + draw()
}

class Client

Client --> Shape : uses
Shape --> Shape : clone()
```