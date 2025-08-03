# Samsa 6 Org Chart

The org chart found in Episode 2, [Fire in the Hole](2025-07-28.md#communications-org-chart)

``` mermaid
flowchart LR
subgraph Civilians
    Hinton["`*Android*<br>**Hinton**`"]

    Edem[Dr. Edem]
    click Edem href "../../people/dr-edem"
    Edem --- Engineering
    Edem --- Science

    subgraph Science
        Ziegler[Dr. Ziegler]
        click Ziegler href "../../people/dr-ziegler"
        Jenson[Dr. Jenson]
        Kawaguchi[Dr. Kawaguchi]
    end

    subgraph Engineering
        Sobol
        Demar
    end
end
subgraph Military
    Kaplan["`*2nd Lt*<br>**Kaplan**`"]
    Lange["`*2nd Lt*<br>**Lange**`"]
    Kaplan & Lange --- Underhill

    Underhill["`*Staff Sgt*<br>**Underhill**`"]
    Underhill --- Valdez

    Valdez["`*Sgt*<br>**Valdez**`"]
    click Valdez href "../../people/valdez"
    Valdez --- Yang & Abarra

    subgraph ZigZag[ZigZag Squad]
        Yang["`*Sgt*<br>**Yang**`"]
        click Yang href "../../people/yang"

        Yang ~~~ Novikov ~~~ Resnick & Xavier ~~~ Tanaka & Pedro & Olsson

        Novikov["`*Cpl*<br>**Novikov**`"]
        click Novikov href "../../people/novikov"

        Resnick["`*Lance Cpl*<br>**Resnick**`"]
        Xavier["`*Lance Cpl*<br>**Xavier**`"]
        Tanaka["`*PFC*<br>**Tanaka**`"]
        Pedro["`*PFC*<br>**Pedro**`"]
        Olsson["`*PFC*<br>**Olsson**`"]
    end

    subgraph Siege[Siege Squad]
        Abarra["`*Sgt*<br>**Abarra**`"]

        Abarra ~~~ Qadir & Ivanovic ~~~ Franco ~~~ Glockner & Weaver ~~~ Brookman

        Qadir["`*Cpl*<br>**Qadir**`"]
        Ivanovic["`*Cpl*<br>**Ivanovic**`"]
        Franco["`*Lance Cpl*<br>**Franco**`"]
        Glockner["`*PFC*<br>**Glockner**`"]
        Weaver["`*PFC*<br>**Weaver**`"]

        Brookman["`*HM3*<br>**Brookman**`"]
        click Brookman href "../../people/brookman"
    end

    classDef alive fill:#464,stroke:#0a0,stroke-width:2px;
    classDef dead fill:#644,stroke:#a00,stroke-width:2px;
    classDef unknown fill:#555,stroke:#aaa,stroke-width:1px;

    class Kawaguchi,Novikov,Pedro,Sobol,Tanaka,Valdez,Yang alive;
    class Brookman,Demar,Franco,Glockner,Ivanovic,Jenson,Kaplan,Lange,Olsson,Qadir,Resnick,Weaver,Xavier,Ziegler dead;
    class Abarra,Hinton,Underhill unknown;
end
```
