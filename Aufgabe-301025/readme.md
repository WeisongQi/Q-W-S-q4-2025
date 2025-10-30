# Aufgabe Heute

    **Anpassen des Plans**

Der Benutzer spricht Chinesisch, hat jedoch um eine Anpassung des Plans gebeten. Da es keine Tools gibt, werde ich mit den Annahmen arbeiten. Ohne klärende Fragen, gemäß den Regeln, aber ich darf anpassen.

Ich werde also ein 4-Wochen-Zeitplan erstellen und zwei Funktionen priorisieren: den Umtausch und den Steuererstattungsrechner sowie den Wetter- und Bekleidungsindex. Weitere Funktionen werden später hinzugefügt. Es gibt Meilensteine, Technologiestandards, Risikomanagement, APIs, Akzeptanzkriterien und einen Wochenplan für Tests und Bereitstellung.

### Projektübersicht

**Projektname:** AI-gestützte Reise-Mini-App (Priorisierte Phase)
**Kurzbeschreibung:** Vierwöchiges Entwicklungsprojekt mit Fokus auf zwei Kernservices: 1) Wechselkurs- und Rückerstattungsrechner für Shopping-Steuern, 2) Lokale Wetterinformationen plus Kleidungs-/Anziehempfehlungen. Weitere Funktionen bleiben als spätere Erweiterungen reserviert.

---

### Projektziele

- **Lieferumfang in 4 Wochen:** Voll funktionsfähiges MVP mit den beiden priorisierten Services.
- **Benutzerwert:** Reisende erhalten schnelle, präzise Umrechnungen und klare Hinweise zur Steuererstattung sowie Wetter- und Kleiderempfehlungen für Entscheidungen unterwegs.
- **Erweiterbarkeit:** Architektur so gestalten, dass weitere Services später einfach ergänzt werden können.

---

### Priorisierter Funktionsumfang

    **Muss-Funktionen (MVP)**

- Wechselkursrechner: aktuelle Kurse, Umrechnung, Anzeige Basis- und Zielwährung, Rundungsoptionen.
- Shopping-Steuerrückerstattungsrechner: Eingabe von Kaufbetrag, MwSt.-Satz, Gebühren/Prozentsatz, berechnete Rückerstattung netto und brutto, erklärender Ablauftext.
- Wetterservice: aktuelles Wetter + 3-Tage-Vorhersage am Nutzerstandort oder eingegebenem Ziel.
- Kleidungs-/Anziehempfehlung: basierend auf Temperatur, Niederschlag, Wind, Saison (vereinfachte Regelbasis + AI-verstärkte Natural Language-Ausgabe).

  **Kann / reserviert**

- Zielgebietinfos, Sehenswürdigkeiten, historische Texte, Offline-Caching, Kartenintegration.

---

### Akzeptanzkriterien (Definition of Done)

- Wechselkurs- und Rückerstattungsrechner liefern korrekte Ergebnisse bei 10 Testfällen (verschiedene Währungen und MwSt.-Sätze).
- Wetter-API integriert, liefert aktuelle Daten und 3-Tage-Vorhersage für gewählten Ort.
- Kleidungs-Empfehlung gibt für fünf Wetterszenarien sensible, verständliche Hinweise.
- UI/UX mobile-responsive, grundlegende Fehlerbehandlung, und Nutzerzustimmung für Standortdaten implementiert.
- Unit- und Integrationstests für Kernlogik vorhanden; Deploy auf Testumgebung automatisiert.

---

### Technische Architektur (Kurz)

- **Frontend:** React (oder HTML/CSS/JS) als Single-Page Mini-App, responsiv.
- **Backend:** Node.js + Express oder Python FastAPI als API-Gateway.
- **Daten:** PostgreSQL für Persistenz (Benutzeroptionen, logs); Redis für kurzfristiges Caching von Wechselkursen und API-Antworten.
- **AI-Komponente:** Leichtgewichtiger Open-Source-Language-Model-Agent für natürliche Erklärtexte und Kleidungs-Empfehlungen; optional gehostet als Inference-Container.
- **Externe Integrationen:** Wechselkurs-API (z. B. fixer, exchangerate.host); Wetter-API (z. B. OpenWeatherMap).
- **Deployment:** Docker-Container, Deployment via GitHub Actions; Hosting in Shared Sandbox (AWS oder Azure) je nach Teamentscheidung.
- **Infrastruktur:** Terraform für IAC optional, je nach Teamkapazität.

---

### Sicherheits- und Datenschutzanforderungen

- **Standortdaten:** Nur mit Einwilligung; Möglichkeit zur manuellen Ortseingabe.
- **Datenminimierung:** Keine personenbezogenen Daten außer optionalem Gerätelabel; Logs pseudonymisiert.
- **Kommunikation:** TLS for API calls.
- **Konformität:** DSGVO-konforme Datenschutzerklärung und Opt-in für Telemetrie.

---

### Meilensteine und 4-Wochen-Zeitrahmen

Woche 0 (Vorbereitungsday, Tag 0)

- Requirements finalisieren; Zugang zu APIs und Sandbox sicherstellen; Repo & CI initialisieren.

Woche 1 — Grundlagen & Wechselkurs-Rechner

- Backend-Grundgerüst + API-Integration Wechselkurs.
- Implementierung Wechselkurs-Handler, Umrechnungs-Logik, Caching.
- Einfaches Frontend für Wechselkurs-UX.
- Unit-Tests für Wechselkurs-Logik.

Woche 2 — Rückerstattungsrechner & erste Integration

- Implementierung MwSt.-/Rückerstattungs-Logik inkl. Gebührenmodelle und Beispiel-Länder.
- UI-Flow für Rückerstattung mit Erklärtexten.
- Integration mit Wechselkursservice (Mehrwährungs-Output).
- Integrationstests und Nutzerfluss-Testing.

Woche 3 — Wetterservice & Kleidungsindex

- Wetter-API-Integration, Location-Handling (Standort-Opt-In + manuelle Eingabe).
- Regelbasierte Kleidungsempfehlungs-Engine entwickeln; AI-Textausgabe für Erklärungen.
- Frontend-Darstellung Wetter + Empfehlung; Fehlerfälle handhaben.

Woche 4 — Stabilisierung, Tests, Beta-Release

- End-to-End-Tests, Usability-Fixes, Performance-Optimierungen.
- CI/CD-Prozess finalisieren; Deployment auf Testumgebung.
- Dokumentation: README, API-Spezifikation, Datenschutz-Text.
- Beta-Release und Vorbereitung für Feedbackrunde; Plan für nächste Feature-Phase.

---

### Rollen und Verantwortlichkeiten (Kernteam, kleine Besetzung)

- **Projektleitung / Product Owner:** Prioritäten, Stakeholder, Zeitplanung.
- **Fullstack-Entwickler:** Backend + Frontend (2 Personen ideal; 1 Person möglich mit längeren Zeiten).
- **AI/Prompt-Engineer:** Kleidungs-Empfehlungen und natürliche Erklärtexte.
- **DevOps:** CI/CD, Deployment, Sandbox-Zugriff, Monitoring (kann geteilt werden).
- **QA / Tester:** Testfälle, Akzeptanztests, Regressionstests.

---

### Qualitäts- und Teststrategie

- Automatisierte Unit-Tests für Umrechnungs- und Rückerstattungslogik.
- Integrationstests für API-Integrationen (Wetter, Wechselkurse).
- Manuelle UI-Tests für kritische Flows (Umrechnung, Rückerstattung, Wetter+Empfehlung).
- Smoke-Tests nach jedem Deploy; einfache Monitoring-Metriken (API-Latenz, Fehler).

---

### Risiken und Gegenmaßnahmen (Kurz)

- API-Limitierungen: Caching, Fallback-Daten für begrenzte Zeit.
- Modell-Inference-Kosten: Verwende leichte Open-Source-Modelle; Default-Regeln als Fallback.
- Datenschutzbedenken: Minimale Standortnutzung, klare Opt-ins.
- Zeitknappheit: Fokus auf Core-Calculations und einfache UX; Erweiterungen auf später verschieben.

---

### Nächste Schritte (sofort ausführbar)

1. Finales Go für MVP-Scope bestätigen (Wechselkurs + Rückerstattung; Wetter + Kleidungsindex).
2. API-Schlüssel für Wechselkurse und Wetter anfordern und testen.
3. Repo und Projektboard (z. B. GitHub Projects) anlegen, Issues für die Week-1-Aufgaben erstellen.
4. Teamrollen festlegen.
