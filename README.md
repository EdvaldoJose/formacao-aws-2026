# Curso Formacao AWS 2026.
### Laboratorio: Abril (x) > Laboratorio: Maio (...)
### Laboratorio: Junho (...) > Laboratorio: Julho (...) 
### Laboratorio: Agosto (...) > Laboratorio: Setembro (...) 
### Laboratorio: Outubro (...) > Laboratorio: Novembro (...) 
##### Duracao do Curso: Maio 2026 / Maio 2027.

| Branch     | Papel           |
| ---------- | --------------- |
| feature    | desenvolvimento |
| developer  | integração      |
| production | validação       |
| main       | produção        |

🧠 POR QUE usar feature/*?
Sem isso:
você quebra developer
mistura código incompleto
dificulta rollback
Com isso:
trabalha isolado
faz PR limpo
CI valida tudo

👉 é padrão de empresa (Git Flow simplificado)

🧨 RESUMO
| Etapa     | Fluxo                  |
| --------- | ---------------------- |
| dev       | feature → developer    |
| validação | developer → production |
| produção  | production → main      |

🧠 REGRA SIMPLES
main = destino final
feature/* → developer → production → main

feature/login-api
   ↓ CI
developer
   ↓ CI
production
   ↓ CD (staging)
main
   ↓ DEPLOY 🚀 (AWS)

🔥 BENEFÍCIO REAL
> não quebra produção
> rollback fácil
> deploy controlado
> pipeline automático