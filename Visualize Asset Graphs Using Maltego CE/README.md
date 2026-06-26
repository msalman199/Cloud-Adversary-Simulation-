
# ☁️ Visualize Asset Graphs Using Maltego CE

<p align="center">

![Maltego](https://img.shields.io/badge/Maltego-Community%20Edition-blue?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04-E95420?style=for-the-badge&logo=ubuntu)
![Java](https://img.shields.io/badge/Java-JRE-orange?style=for-the-badge&logo=openjdk)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Analysis-green?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple?style=for-the-badge&logo=pandas)
![CSV](https://img.shields.io/badge/Data-CSV-yellow?style=for-the-badge)
![GraphML](https://img.shields.io/badge/Export-GraphML-success?style=for-the-badge)
![Cyber Security](https://img.shields.io/badge/Cyber-Security-red?style=for-the-badge)

</p>

---

# 📖 Overview

Graph visualization is one of the most effective ways to understand cloud infrastructure, attack surfaces, and relationships between digital assets.

In this lab you will learn how to use **Maltego Community Edition (CE)** to visualize domains, IP addresses, services, and email addresses, allowing you to understand infrastructure relationships from a graphical perspective.

Instead of viewing thousands of assets in text files, Maltego transforms them into interactive relationship graphs that are invaluable during:

- 🔍 Reconnaissance
- ☁️ Cloud Asset Discovery
- 🛡️ Security Assessments
- 🎯 Red Team Operations
- 🕵️ Threat Hunting
- 📊 Infrastructure Analysis

---

# 🎯 Learning Objectives

After completing this lab you will be able to:

- ✅ Install Maltego Community Edition on Linux
- ✅ Configure Maltego CE
- ✅ Import cloud asset data
- ✅ Build interactive asset relationship graphs
- ✅ Visualize domains, IPs, emails and services
- ✅ Understand graph-based reconnaissance
- ✅ Use Maltego transforms
- ✅ Discover hidden relationships
- ✅ Export graphs for reporting
- ✅ Prepare graph data using Python

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Maltego CE | Asset Visualization |
| Ubuntu Linux | Lab Platform |
| Java Runtime | Maltego Dependency |
| Python 3 | Automation |
| Pandas | Data Processing |
| NetworkX | Graph Analysis |
| Matplotlib | Graph Visualization |
| CSV | Data Import |
| GraphML | Graph Export |

---

# 📚 Prerequisites

Before beginning this lab you should understand:

- Linux command line
- DNS concepts
- IP addressing
- Cloud infrastructure
- Network services
- Basic cybersecurity concepts
- Asset discovery fundamentals
- Python basics

---

# 🖥️ Lab Environment

The lab environment includes:

- Ubuntu 22.04 LTS
- Internet connectivity
- Java support
- Python 3
- Sample cloud asset files
- Required Linux packages

---

# 📂 Lab Structure

```
Visualize Asset Graphs Using Maltego CE
│
├── Task 1
│   ├── Install Maltego
│   └── Configure Maltego
│
├── Task 2
│   ├── Prepare Asset Data
│   └── Create Relationships
│
├── Task 3
│   ├── Import Data
│   └── Create Graph
│
├── Task 4
│   ├── Link Assets
│   └── Organize Graph
│
├── Task 5
│   ├── Use Transforms
│   └── Discover Assets
│
├── Task 6
│   ├── Graph Analysis
│   └── Entity Groups
│
├── Task 7
│   ├── Export Graph
│   └── Create Reports
│
├── Task 8
│   └── Python Automation
│
└── Task 9
    └── Advanced Features
```

---

# 🚀 Task 1 — Install and Configure Maltego CE

---

# 🔹 Step 1.1 — Install Maltego Community Edition

Update system packages.

```bash
sudo apt update && sudo apt upgrade -y
```

---

Install Java Runtime Environment.

```bash
sudo apt install default-jre -y
```

---

Verify Java installation.

```bash
java -version
```

Expected output:

```text
openjdk version "11.x.x"
```

---

Navigate to the Downloads directory.

```bash
cd ~/Downloads
```

---

Download Maltego Community Edition.

```bash
wget https://maltego-downloads.s3.us-east-2.amazonaws.com/linux/Maltego.v4.5.0.deb
```

---

Install Maltego.

```bash
sudo dpkg -i Maltego.v4.5.0.deb
```

---

Resolve missing dependencies if necessary.

```bash
sudo apt-get install -f
```

---

# 🔹 Step 1.2 — Configure Maltego CE

Launch Maltego.

```bash
maltego
```

When the application opens:

1. Register a free Maltego account.
2. Verify your email.
3. Log in.
4. Select **Maltego Community Edition**.
5. Accept the license agreement.
6. Complete the setup wizard.

---

# ✅ Task 1 Complete

You should now have:

- Java installed
- Maltego installed
- Community Edition activated
- Ready for graph creation

---

# 🚀 Task 2 — Prepare Sample Asset Data

---

# 🔹 Step 2.1 — Create Working Directory

Create a workspace.

```bash
mkdir ~/maltego_lab
```

Move into it.

```bash
cd ~/maltego_lab
```

---

# 🔹 Step 2.2 — Create Domain List

Create:

```text
domains.txt
```

```bash
cat > domains.txt << EOF
example-corp.com
api.example-corp.com
mail.example-corp.com
cdn.example-corp.com
admin.example-corp.com
dev.example-corp.com
staging.example-corp.com
EOF
```

Verify contents.

```bash
cat domains.txt
```

---

# 🔹 Step 2.3 — Create IP Address List

Create:

```text
ip_addresses.txt
```

```bash
cat > ip_addresses.txt << EOF
203.0.113.10
203.0.113.11
203.0.113.12
198.51.100.5
198.51.100.6
192.0.2.100
192.0.2.101
EOF
```

Verify.

```bash
cat ip_addresses.txt
```

---

# 🔹 Step 2.4 — Create Service List

Create:

```text
services.txt
```

```bash
cat > services.txt << EOF
HTTP,80,203.0.113.10
HTTPS,443,203.0.113.10
SSH,22,203.0.113.11
MySQL,3306,203.0.113.12
Redis,6379,198.51.100.5
MongoDB,27017,198.51.100.6
Elasticsearch,9200,192.0.2.100
EOF
```

Verify.

```bash
cat services.txt
```

---

# 🔹 Step 2.5 — Create Email List

Create:

```text
emails.txt
```

```bash
cat > emails.txt << EOF
admin@example-corp.com
support@example-corp.com
security@example-corp.com
dev@example-corp.com
info@example-corp.com
EOF
```

Verify.

```bash
cat emails.txt
```

---

# 🔹 Step 2.6 — Create Relationship Data

Create:

```text
relationships.csv
```

```bash
cat > relationships.csv << EOF
Source,Relationship,Target
example-corp.com,resolves_to,203.0.113.10
api.example-corp.com,resolves_to,203.0.113.11
mail.example-corp.com,resolves_to,203.0.113.12
admin@example-corp.com,belongs_to,example-corp.com
support@example-corp.com,belongs_to,example-corp.com
203.0.113.10,runs_service,HTTP
203.0.113.10,runs_service,HTTPS
203.0.113.11,runs_service,SSH
203.0.113.12,runs_service,MySQL
EOF
```

Verify.

```bash
cat relationships.csv
```

---

# 📋 Current Lab Files

After completing Task 2, your working directory should contain:

```text
maltego_lab/
│
├── domains.txt
├── ip_addresses.txt
├── services.txt
├── emails.txt
└── relationships.csv
```

---

# ✅ Task 2 Complete

You have successfully prepared:

- 🌐 Domain inventory
- 🌍 IP address inventory
- 📧 Email addresses
- ⚙️ Service information
- 🔗 Asset relationship data

The next section will import these assets into **Maltego Community Edition** and begin building interactive relationship graphs.
````
````markdown
---

# 🚀 Task 3 — Import Asset Data into Maltego

Now that the sample asset files have been created, it's time to import them into **Maltego Community Edition** and begin constructing an interactive asset relationship graph.

---

# 🔹 Step 3.1 — Create a New Graph

Launch **Maltego CE**.

```bash
maltego
```

Once the application opens:

1. Click **New Graph**
2. Or press:

```text
Ctrl + N
```

You should now see an empty workspace with the **Entity Palette** on the left side.

---

## 💾 Save Your Graph

Press

```text
Ctrl + S
```

Save the project as:

```text
Cloud_Asset_Analysis
```

Your graph file will now store all future entities and relationships.

---

# 🔹 Step 3.2 — Add Domain Entities

Locate the **Infrastructure** category.

Choose:

```text
Infrastructure
    └── Domain
```

Drag a **Domain** entity onto the canvas.

Double-click the entity.

Change its value to:

```text
example-corp.com
```

Repeat for every domain.

```text
example-corp.com
api.example-corp.com
mail.example-corp.com
cdn.example-corp.com
admin.example-corp.com
dev.example-corp.com
staging.example-corp.com
```

---

### ✅ Result

Your graph should now contain seven Domain entities.

```
example-corp.com

api.example-corp.com

mail.example-corp.com

cdn.example-corp.com

admin.example-corp.com

dev.example-corp.com

staging.example-corp.com
```

---

# 🔹 Step 3.3 — Add IPv4 Address Entities

From the Entity Palette choose

```text
Infrastructure
      └── IPv4 Address
```

Create IPv4 entities for each address.

```
203.0.113.10

203.0.113.11

203.0.113.12

198.51.100.5

198.51.100.6

192.0.2.100

192.0.2.101
```

---

### 💡 Tip

Arrange IPs underneath the domains to improve readability.

---

# 🔹 Step 3.4 — Add Email Entities

Locate

```text
Personal

    └── Email Address
```

Add the following email addresses.

```
admin@example-corp.com

support@example-corp.com

security@example-corp.com

dev@example-corp.com

info@example-corp.com
```

---

# 📊 Current Graph

At this point your graph contains approximately:

```
7 Domains

7 IPv4 Addresses

5 Email Addresses
```

Total:

```
19 Entities
```

---

# ✅ Task 3 Complete

Your graph now contains the primary cloud assets required for relationship mapping.

---

# 🚀 Task 4 — Visualize Relationships Between Assets

The power of Maltego comes from visualizing relationships instead of viewing isolated assets.

---

# 🔹 Step 4.1 — Create Manual Relationships

Right-click a source entity.

Choose

```
Links

    └── Add Link
```

Click the destination entity.

Create these relationships.

---

## DNS Relationships

```
example-corp.com

↓

203.0.113.10
```

```
api.example-corp.com

↓

203.0.113.11
```

```
mail.example-corp.com

↓

203.0.113.12
```

---

## Email Relationships

```
admin@example-corp.com

↓

example-corp.com
```

```
support@example-corp.com

↓

example-corp.com
```

```
security@example-corp.com

↓

example-corp.com
```

```
dev@example-corp.com

↓

example-corp.com
```

```
info@example-corp.com

↓

example-corp.com
```

---

# 🔹 Step 4.2 — Customize Link Properties

Right-click a relationship.

Choose

```
Properties
```

Modify:

- Link Label
- Link Color
- Thickness
- Style

Recommended color scheme.

| Relationship | Color |
|-------------|--------|
| DNS Resolution | 🔵 Blue |
| Ownership | 🟢 Green |
| Service Mapping | 🔴 Red |

---

Example:

```
example-corp.com

────── resolves to ──────►

203.0.113.10
```

---

# 🔹 Step 4.3 — Organize Graph Layout

Select every entity.

```
Ctrl + A
```

Choose

```
Layout

↓

Hierarchical
```

Other useful layouts include

- Organic
- Circular
- Symmetric
- Radial

---

### Example Layout

```
                 example-corp.com
                     /     \
                    /       \
                   /         \
          api              mail
             \              /
              \            /
               \          /
               203.0.113.10
```

---

### Fine Tune

Move entities manually until

- Links don't overlap
- Groups remain readable
- Parent assets stay above children

---

# ✅ Task 4 Complete

Your graph should now clearly illustrate

- Domain ownership
- DNS mappings
- Email ownership
- Infrastructure relationships

---

# 🚀 Task 5 — Use Maltego Transforms

Transforms automatically discover additional relationships.

This is one of Maltego's most powerful features.

---

# 🔹 Step 5.1 — DNS Resolution Transform

Select

```
example-corp.com
```

Right-click.

Choose

```
Run Transform

↓

DNS

↓

To IP Address [DNS]
```

Maltego will perform DNS resolution.

New IP entities will automatically appear.

---

Repeat for

```
api.example-corp.com

mail.example-corp.com

cdn.example-corp.com

admin.example-corp.com

dev.example-corp.com
```

---

# 🔹 Step 5.2 — Reverse DNS

Select an IP address.

Example

```
203.0.113.10
```

Choose

```
Run Transform

↓

DNS

↓

To Domain [DNS]
```

Maltego attempts reverse lookup.

Possible results

```
www.example-corp.com

cdn.example-corp.com

mail.example-corp.com
```

---

# 🔹 Step 5.3 — Email Domain Transform

Select

```
admin@example-corp.com
```

Choose

```
Run Transform

↓

Email

↓

To Domain
```

Maltego extracts

```
example-corp.com
```

and automatically creates the relationship.

Repeat for

```
support@example-corp.com

security@example-corp.com

dev@example-corp.com

info@example-corp.com
```

---

# 📈 Graph Growth

Before transforms

```
19 Entities
```

After transforms

```
25+

30+

40+
```

depending on discovered infrastructure.

---

# 💡 Why Use Transforms?

Transforms allow security analysts to

- Discover hidden infrastructure
- Identify forgotten assets
- Expand attack surface mapping
- Correlate domains and services
- Reveal cloud relationships

without manual investigation.

---

# 🔍 Example Asset Graph

```
                 example-corp.com
                      │
      ┌───────────────┼───────────────┐
      │               │               │
      ▼               ▼               ▼

 api.example     mail.example     cdn.example

      │               │               │

      ▼               ▼               ▼

203.0.113.11   203.0.113.12   198.51.100.5

      │               │               │

      ▼               ▼               ▼

 SSH           MySQL Service      HTTPS
```

---

# ✅ Task 5 Complete

You have successfully learned how to

- Execute DNS transforms
- Perform reverse DNS lookups
- Extract domains from email addresses
- Automatically expand infrastructure graphs
- Discover relationships using Maltego transforms

In the next section, you'll perform **advanced graph analysis**, create **entity groups**, apply **filters**, and export professional reports from your asset graph.
````
````markdown id="maltego_part3"
---

# 🚀 Task 6 — Advanced Graph Analysis

Now that your Maltego graph contains domains, IPs, emails, and service relationships, we will move into **advanced graph analysis techniques** used in real-world cloud security assessments.

---

# 🔹 Step 6.1 — Add Service Information

From the **Entity Palette**, locate:

```text
Infrastructure → Service
```

Add service entities for common cloud services:

```
HTTP (80)
HTTPS (443)
SSH (22)
MySQL (3306)
Redis (6379)
MongoDB (27017)
Elasticsearch (9200)
```

---

## 🔗 Link Services to IPs

Create relationships based on `services.txt`:

```
203.0.113.10 → HTTP
203.0.113.10 → HTTPS
203.0.113.11 → SSH
203.0.113.12 → MySQL
198.51.100.5 → Redis
198.51.100.6 → MongoDB
192.0.2.100 → Elasticsearch
```

---

## 📊 Resulting Structure

```
           IP Address
                │
                ▼
           Services
```

This reveals:

- Exposed ports
- Running applications
- Infrastructure roles

---

# 🔹 Step 6.2 — Create Entity Groups

Grouping helps reduce graph complexity.

---

## 📦 Create Groups

Select multiple entities using:

```text
Ctrl + Click
```

Then:

```text
Right Click → Group → Create Group
```

---

## 🏷 Recommended Groups

### 🌐 Web Services Group

```
HTTP
HTTPS
api.example-corp.com
cdn.example-corp.com
```

---

### 🗄 Database Group

```
MySQL
MongoDB
Redis
Elasticsearch
```

---

### 📧 Email Infrastructure Group

```
admin@example-corp.com
support@example-corp.com
security@example-corp.com
```

---

## 🎯 Why Grouping Matters

Grouping allows you to:

- Reduce visual clutter
- Identify attack surfaces
- Segment infrastructure
- Understand architecture layers

---

# 🔹 Step 6.3 — Apply Filters and Views

Filters help you focus on specific asset types.

---

## 🧭 Enable Filters

Go to:

```text
View → Filters
```

Select:

- Domains only
- IP addresses only
- Services only
- Emails only

---

## 👁️ Visualization Options

Toggle:

- Entity Labels ✔
- Link Labels ✔
- Icons instead of text ✔

---

## 🎨 Recommended View Setup

| Option | Setting |
|--------|--------|
| Labels | ON |
| Icons | ON |
| Links | ON |
| Background | Dark |

---

# 🚀 Task 7 — Export and Document Findings

Once your graph is complete, you must export findings for reporting.

---

# 🔹 Step 7.1 — Export Graph Image

Navigate to:

```text
File → Export → Export Graph to Image
```

Select:

- Format: PNG
- Resolution: High (300 DPI)

Save as:

```text
cloud_asset_graph.png
```

---

## 📸 Use Case

This image is used in:

- Security reports
- Client presentations
- Audit documentation
- Threat modeling reports

---

# 🔹 Step 7.2 — Export Graph Data

Export graph structure:

```text
File → Export → GraphML
```

Save as:

```text
cloud_assets.graphml
```

---

## 📌 Why GraphML?

GraphML allows:

- Import into NetworkX
- Advanced analytics
- Machine learning analysis
- External graph tools

---

# 🔹 Step 7.3 — Generate Asset Report

Create a structured report:

```bash
cat > asset_analysis_report.txt << EOF
Cloud Asset Analysis Report
===========================

Graph Summary:
- Total Entities: [Calculated in Maltego]
- Domains: example-corp.com, api.example-corp.com, mail.example-corp.com
- IP Addresses: 7 discovered IPs
- Email Addresses: 5 corporate emails
- Services: HTTP, HTTPS, SSH, Databases

Key Relationships:
- DNS resolution mappings
- Email ownership hierarchy
- Service-to-IP mappings

Security Observations:
- Exposed services detected
- Public-facing IP infrastructure
- Potential misconfigured services

Recommendations:
- Restrict database exposure
- Harden SSH access
- Monitor API endpoints
- Implement network segmentation
EOF
```

---

# 🚀 Task 8 — Automate Graph Preparation with Python

Now we automate asset preparation for Maltego-style analysis.

---

# 🔹 Step 8.1 — Install Dependencies

```bash
sudo apt install python3-pip -y
pip3 install pandas networkx matplotlib
```

---

# 🔹 Step 8.2 — Create Graph Analysis Script

Create file:

```text
prepare_maltego_data.py
```

---

## 🐍 Python Script

```python
#!/usr/bin/env python3

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def create_asset_graph():
    """
    Build graph from relationships.csv
    """

    G = nx.Graph()

    try:
        df = pd.read_csv("relationships.csv")

        for _, row in df.iterrows():
            G.add_edge(row["Source"], row["Target"], relationship=row["Relationship"])

        print("\n[+] Graph Created")
        print(f"Nodes: {G.number_of_nodes()}")
        print(f"Edges: {G.number_of_edges()}")

        print("\n[+] Analysis Results")

        print("Density:", nx.density(G))
        print("Components:", nx.number_connected_components(G))

        centrality = nx.degree_centrality(G)
        top_node = max(centrality, key=centrality.get)

        print("Most Connected Asset:", top_node)

        # Visualization
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, seed=42)

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=1500,
            font_size=8
        )

        plt.title("Cloud Asset Relationship Graph")
        plt.savefig("asset_graph.png", dpi=300)

        print("\n[+] Graph saved as asset_graph.png")

        return G

    except FileNotFoundError:
        print("relationships.csv not found")
        return None


def export_data(G):
    """
    Export Maltego-compatible data
    """

    if not G:
        return

    nodes = []

    for node in G.nodes():
        if "@" in node:
            t = "Email"
        elif node.replace(".", "").isdigit():
            t = "IPv4"
        elif "." in node:
            t = "Domain"
        else:
            t = "Service"

        nodes.append([node, t])

    pd.DataFrame(nodes, columns=["Entity", "Type"]).to_csv("entities.csv", index=False)

    edges = []

    for u, v, d in G.edges(data=True):
        edges.append([u, v, d.get("relationship", "linked")])

    pd.DataFrame(edges, columns=["Source", "Target", "Relationship"]).to_csv("edges.csv", index=False)

    print("[+] Export completed: entities.csv, edges.csv")


if __name__ == "__main__":
    graph = create_asset_graph()
    export_data(graph)
```

---

## ▶ Run Script

```bash
python3 prepare_maltego_data.py
```

---

## 📁 Output Files

```
asset_graph.png
entities.csv
edges.csv
```

---

# 📊 What You Achieved

You now have:

- ✔ Graph-based asset model
- ✔ Relationship extraction
- ✔ Centrality analysis
- ✔ Visualization generation
- ✔ Maltego-compatible exports

---

# ✅ Task 8 Complete

You now understand how to:

- Convert raw asset data into graph structures
- Analyze relationships programmatically
- Visualize infrastructure using Python
- Export data for Maltego integration

---

# ⏭ Next Section

In **Part 4**, you will complete the lab with:

- Advanced Maltego features
- Custom entity creation
- CSV import automation
- Troubleshooting guide
- Final conclusions and security insights
````
---

# 🚀 Task 9 — Advanced Maltego Features (Final Stage)

In this final section, you will extend your Maltego workflow into a **real-world threat intelligence and asset correlation system**.

---

# 🔹 Step 9.1 — Create Custom Entity Types

Maltego allows you to define **custom entities** for better cloud asset modeling.

---

## ⚙ Open Entity Manager

Navigate to:

```text
Manage → Manage Entities

