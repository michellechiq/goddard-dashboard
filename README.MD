# Goddard Riverside Community Portal
### Data Pipeline & Reporting Dashboard
**Developed by Michelle**

## Project Overview
This project implements a structured, auditable data pipeline that transforms raw submissions into clean, analysis-ready datasets for reporting in **Looker Studio**. The system is hosted via a **Streamlit** web interface, providing a single point of access for Goddard Riverside staff to view analytics, interact with live data, and submit new information.

## Branding & Aesthetics
To maintain institutional consistency, the portal follows the Goddard Riverside style guide:
- **Font:** Droid Serif (Classic/Institutional feel)
- **Primary Red:** `#A50034` (Goddard Red)
- **Background:** `#FAF7EB` (Goddard Cream)
- **Primary Text:** `#49280D` (Dark Brown)

## Data Quality & Jotform Guardrails
Data integrity begins at the point of entry. The Jotform is configured with strict validation to minimize "dirty data":
* **Integer Validation:** Numeric fields (e.g., staff counts) strictly prohibit decimal entries. Users are blocked from proceeding if non-integers are detected.
* **Real-time Guidance:** Warning signs and reminders are embedded in the form to ensure staff understand specific data definitions before hitting submit.
* **Hard Blocks:** Prevents invalid data from ever reaching the Google Sheet, reducing manual QA time.

## Limitations and Assumptions
* **Primary Key Constraint:** The system identifies records by `program_name`. It is assumed that each program submits exactly once. 
* **Duplicate Handling:** Because the `program_name` acts as the primary key, duplicate submissions for the same program will cause inflated metrics and must be manually reconciled in the `Clean_Data` tab.
* **Input Accuracy:** The system relies on the accuracy of content provided by Directors and Assistant Directors.
* **Typo Prevention:** Users are expected to select program names from provided options to avoid "dirty" keys (e.g., "MnIS" vs "Manhattan In-reach Services") that would break data joins.

---

## Data Pipeline Structure (Google Sheets)

### 1. Form Responses 1 (Raw Data)
* **Input:** Real-time population via the **Jotform Google Sheets Integration tool**.
* **Behavior:** New submissions are appended as new rows; existing rows are preserved for an immutable audit trail.

### 2. Clean_Data (Primary Reporting Table)
This tab acts as the primary "Reporting View" for Looker Studio, representing one program per row.
* **Standardization:** Names/Titles are Proper Cased; abbreviations (Asst, Sr, Jr) are expanded via formulas.
* **Address Normalization:** City values (NY, BK, BX) are converted to full names (New York, Brooklyn, Bronx).
* **Type Conversion:** Ensures all Jotform "text" numbers are forced into "Numeric" formats for calculation.

### 3. Dimensional Tables (Long / Reshaped Data)
To enable dynamic filtering, specific categories are reshaped from wide to long format. This allows Looker Studio to treat these as selectable dimensions rather than static metrics.

| Table Name | Definition |
| :--- | :--- |
| **dim_gender** | Flattens gender identity responses. Allows for multiple selections per program. |
| **dim_age_group** | Consolidates multiple age-band columns into a single "Age Group" dimension for lifecycle reporting. |
| **dim_race_ethnicity** | Reshapes demographic data to allow for categorical filtering by race or ethnic background. |
| **dim_education** | Normalizes educational attainment levels (e.g., High School, Bachelor's) per program. |
| **system_usage** | Parses the `data_systems_raw` field to list individual software systems (e.g., Salesforce, PeerPlace) used by each program. |

**Reshaping Formula Example (Unpivoting Logic):**
``excel
=ARRAYFORMULA(
  QUERY(
    SPLIT(
      FLATTEN(
        FILTER(INDEX(Clean_Data!A:AAG,,MATCH("program_name",Clean_Data!1:1,0)),ROW(Clean_Data!A:A)>1) & "♦" &
        TRIM(
          SPLIT(
            REGEXREPLACE(
              FILTER(INDEX(Clean_Data!A:AAG,,MATCH("data_systems_raw",Clean_Data!1:1,0)),ROW(Clean_Data!A:A)>1),
              "\s*\n\s*",
              ","
            ),
            ","
          )
        )
      ),
      "♦"
    ),
    "where Col2 is not null",
    0
  )
)

## Looker Studio Integration
* **Data Sources:** Joins `Clean_Data` with the `dim_` tables using **program_name** as the primary join key.
* **Metric Calculation:** When using dimension tables, **COUNT DISTINCT (program_name)** must be used to ensure programs are not overcounted due to the one-to-many relationship created by reshaping.
* **Global Controls:** Master filters for "Program Name" and "Borough" update every chart simultaneously across all data sources.

## Technical Setup (Streamlit)
The dashboard UI is customized via CSS to override default styles with Droid Serif and Goddard Red.

**Requirements:**
- Python 3.x
- `streamlit`

**Deployment:**
The app is deployed via **Streamlit Community Cloud**, linked directly to the GitHub repository.

---

## Governance & Maintenance
* **Audit Trail:** Never modify "Form Responses 1". 
* **Logic Updates:** Any changes to cleaning or abbreviations should be done in the `Clean_Data` formulas.
* **Key Integrity:** If a program is renamed in Jotform, it must be updated across all sheets to maintain the join.