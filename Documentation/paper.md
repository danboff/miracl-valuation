---
title: 'Distributed Wind Valuation Service'
tags:
  - renewable energy
  - distributed wind energy
  - distributed energy resources
  - valuation 

authors:
  - name:  Bilal Ahmad Bhatti
    orcid: 0000-0003-2149-1163
    equal-contrib: false
    affiliation: 1
     equal-contrib: 
 - name:   Andrew Reiman
    orcid: 0000-0003-0204-2960
    equal-contrib: false
    affiliation: 1
- name:   Daniel Boff
    orcid: 0000-0002-7829-3873
    equal-contrib: false
    affiliation: 1
- name:  Sarah Barrows 
    orcid: 
    equal-contrib: false
    affiliation: 1
 - name: Alice Orrell 
    orcid: 0000-0002-9418-9451
    equal-contrib: false
    affiliation: 1
affiliations:
 - name: Pacific Northwest National Laboratory
   index: 1
date: 13 August 2017
bibliography: paper.bib
---
# Summary
As the electricity system becomes more renewable and distributed, an increasingly diverse set of technologies will need to be compared and evaluated. These technologies may create different values, which may accrue to a diverse set of stakeholders. Distributed wind has the ability to deliver a broad set of benefits, ranging from electricity generation to pollution reduction, ancillary services, renewable energy credits, as well as reduced peak capacity charges. However, these values are often poorly understood and difficult to calculate. This software allows users to better understand this flow of benefits. Users can then use these findings to assist in cost-benefit analysis, compare distributed wind to other resources, and identify potential high value operations for their projects.   

# Statement of need
Although there is a growing market for distributed wind technology, the industry lacks consistent and transparent methods for evaluating the costs and benefits of distributed wind [@BARROWS2021111678]. Beginning in 2021, the Pacific Northwest National Laboratory developed a framework for valuing distributed wind projects [@osti_1777484]. While this methodology has been used in two case study applications [@en14216956; @osti_1875831] it does not exist as a broadly accessible calculation service. 

A variety of stakeholders provided feedback that informed the development of such a service. Developers indicated that a consistent, third-party developed framework could be used to help potential offtakers understand the value streams associated with their systems. As many current analytical methods are based solely on project revenues, a broader focus could help buyers understand the nonmonetary benefits of distributed wind. From the utility or rural electric cooperative’s perspective, a valuation service could be useful in evaluating third-party bids and ensuring that any power purchase agreement they agree to is a fair assessment of the project’s value. Policymakers also indicated that improved valuation software could help inform policies like net metering and other incentives.  

In order to improve the usability of the framework, we have developed a service that allows users to better understand and optimize the value of a distributed wind project and identify to which stakeholders these values accrue. This Python-based service is capable of calculating values for energy generation, avoided carbon dioxide emissions, demand charges, and reduction in on-peak load charges from generation and transmission utilities. It is capable of calculating values for both behind- and front-of-the-meter systems and recognizing hourly variations in prices. The service also has a unique co--optimization function. For mutually exclusive value streams, the service can weigh the relative values of each and display values for the optimal operational strategy. This analysis can help inform operations strategies in addition to valuation exercises. The distributed wind valuation service was designed to assist developers, utilities energy engineers, economists, and policy makers interested in distributed wind and distributed energy resources, in general. It can assist in decision making by allowing users to weigh direct and societal benefits stemming from a distributed wind project. The service could also be expanded with additional analysis to identify high value operational strategies, that could result from wind projects participating in non-traditional markets like reserve or regulation markets. 

# Acknowledgements
This work was funded by the Department of Energy's Wind Energy Technologies Office 

# References
