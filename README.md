# llm_guide

```mermaid
%%{ init : { "theme": "default", "themeVariables": {
  "primaryColor": "#0A0A0A",
  "primaryTextColor": "#FFFFFF",
  "primaryBorderColor": "#D9D9D9"
}}}%%
graph TD
  A[Start]:::core --> B{Logic}:::logic
  B -->|Yes| C[Action]:::action

  classDef core fill:#0A0A0A,stroke:#D9D9D9,color:#FFFFFF;
  classDef logic fill:#002B5C,stroke:#9EA1A6,color:#FFFFFF;
  classDef action fill:#C8102E,stroke:#9EA1A6,color:#FFFFFF;
  ```
  