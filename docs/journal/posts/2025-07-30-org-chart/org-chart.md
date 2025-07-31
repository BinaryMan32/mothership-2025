---
date: 2025-07-30T00:00:00
module: Another Bug Hunt
title: Org Chart
---
# {{ page.meta.module }}: {{ page.meta.title }}

The org chart found in Episode 2, [Fire in the Hole](2025-07-28.md#communications-org-chart)

<!-- more -->

{% include 'module_episode_list.md' %}

``` mermaid
flowchart TD
subgraph Research
    Edem[Dr. Edem]
    click Edem href "../../../../../people/dr-edem"
    Edem --- Hinton["Hinton(Android)"]
    Hinton --- Ziegler[Dr. Ziegler]
    Ziegler --- Jenson[Dr. Jenson]
    Jenson --- Kawaguchi[Dr. Kawaguchi]
end
subgraph Military
    Underhill["`*Staff Sgt*<br>**Underhill**`"]
    Underhill --- Lange
    Underhill --- Valdez
    Underhill --- Qadir
    Underhill --- Abarra

    subgraph Greta[Greta Base]
        Lange["`*2nd Lt*<br>**Lange**`"]
        Lange --- Kaplan["`*2nd Lt*<br>**Kaplan**`"]
        Kaplan --- Resnick["`*Lance Cpl*<br>**Resnick**`"]
        Resnick --- Olsson["`*PFC*<br>**Olsson**`"]
    end

    subgraph Terraforming[Terraforming Base]
        Valdez["`*Sgt*<br>**Valdez**`"]
        click Valdez href "../../../../../people/valdez"
        Valdez --- Yang["`*Sgt*<br>**Yang**`"]
        click Yang href "../../../../../people/yang"
        Yang --- Novikov["`*Cpl*<br>**Novikov**`"]
        click Novikov href "../../../../../people/novikov"
        Novikov --- Ivanovic["`*Cpl*<br>**Ivanovic**`"]
        Ivanovic --- Brookman["`*HM3*<br>**Brookman**`"]
        click Brookman href "../../../../../people/brookman"
    end

    subgraph Siege[Siege Squad]
        Qadir["`*Cpl*<br>**Qadir**`"]
        Qadir --- Franco["`*Lance Cpl*<br>**Franco**`"]
        Franco --- Glockner["`*PFC*<br>**Glockner**`"]
        Glockner --- Weaver["`*PFC*<br>**Weaver**`"]
    end

    subgraph Unknown
        Abarra["`*Sgt*<br>**Abarra**`"]
        Abarra --- Xavier["`*Lance Cpl*<br>**Xavier**`"]
        Xavier --- Tanaka["`*PFC*<br>**Tanaka**`"]
        Tanaka --- Pedro["`*PFC*<br>**Pedro**`"]
        Pedro --- Sobol["`*Engineer*<br>**Sobol**`"]
        Sobol --- Demar
    end

    classDef alive fill:#464,stroke:#0a0,stroke-width:2px;
    classDef dead fill:#644,stroke:#a00,stroke-width:2px;
    classDef unknown fill:#555,stroke:#aaa,stroke-width:1px;

    class Kawaguchi,Novikov,Sobol,Valdez,Yang alive;
    class Brookman,Franco,Glockner,Ivanovic,Jenson,Kaplan,Lange,Olsson,Qadir,Resnick,Weaver,Xavier,Ziegler dead;
    class Abarra,Demar,Hinton,Pedro,Tanaka,Underhill unknown;
end
```
