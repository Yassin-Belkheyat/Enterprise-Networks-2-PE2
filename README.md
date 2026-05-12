# Enterprise-Networks-2-PE2

## Beschrijving
 Dit project automatiseert een Cisco IOS-XE router via RESTCONF en Python, gebaseerd op YANG-modellen.De configuratie wordt programmatisch toegepast vanuit JSON-configuratiebestanden en beheerd via GitHub als     single source of truth.
## Functionaliteiten
 Het script configureert automatisch:
  - Hostname
  - Loopback0 interface
  - IPv4-adres configuratie
  - OSPF process
  
  Daarnaast voert het script RESTCONF GET-operaties uit om de configuratie te valideren.
## Gebruikte technologieën
  - Python 3
  - RESTCONF
  - Cisco IOS-XE YANG-modellen
  - GitHub
  - YANG Suite
## Gebruikte YANG-modellen
### Cisco-IOS-XE-native
  Gebruikt voor:
  - hostname configuratie
  - interface configuratie
  - IP-adressen
### Cisco-IOS-XE-ospf
  Gebruikt voor:
  - OSPF configuratie
  - network statements

