# AHP-Based Vulnerability Assessment of Gas Stations

## Repository Overview
/ahp-data-analysis  
│── /data/datasets             
│── /notebooks                  
│── /results                   
│── /src  
│   │── config.yaml             
│   │── data_loader.py          
│   │── data_processing.py     
│   │── ahp_analysis.py          
│   │── main.py                   
│── requirements.txt            
│── README.md                   


## Project Overview
This project focuses on developing methodologies and intelligent information technologies for assessing the vulnerability of gas stations to various types of accidents. The work is part of a Ukrainian-British collaborative project that aims to enhance safety, emergency response, and risk management for critical infrastructure, particularly gas stations.

The project involves the development of a multi-criteria vulnerability assessment model that incorporates various factors such as economic, social, and environmental risks. By leveraging advanced data analytics, expert evaluations, and the Analytic Hierarchy Process (AHP), the project aims to provide decision-makers with a reliable tool for assessing vulnerability and prioritizing mitigation strategies. 

The method includes expert surveys, pairwise comparison matrices, and ranking automation for getting the priorities all of factors. The developed system reduces manual evaluation time by **4.5x** while maintaining high correlation with traditional methods.

## Key Features 
- **Data Collection & Processing**: Gathered and processed data from gas stations to assess their vulnerability across multiple criteria.
- **Expert Evaluation**: A web-based system was developed for surveying experts on vulnerability factors using ranking methods.
- **AHP Methodology**: A decision support system was built based on the Analytic Hierarchy Process (AHP) to rank vulnerability factors and compute priority vectors.
- **Automation**: Automated the processing of expert assessments, generation of pairwise comparison matrices, and evaluation of results.
- **Visualization**: Integrated data visualization techniques to display the analysis results and provide actionable insights.

## Objectives
- Assess the vulnerability of gas stations to various risks and accidents.
- Develop an intelligent information technology system to assist in vulnerability assessment.
- Automate expert evaluations and calculations using Python, Django, and PostgreSQL.
- Visualize and present results to facilitate decision-making for risk management and safety measures.

## Technologies Used
- **Python**: For data analysis, statistical modeling, and automation.
- **Django**: For the development of the expert survey system.
- **PostgreSQL**: For data storage and management.
- **Matplotlib, Seaborn**: For data visualization and plotting.
- **Fuzzy Logic**: For interpreting vulnerability assessments.

## Methodology
1. **Expert Surveys**: Experts provide rankings of various vulnerability factors for gas stations.
2. **Data Processing**: Process the expert rankings using the AHP to calculate priority vectors and consistency indices.
3. **Multi-Criteria Analysis**: Evaluate the vulnerability of gas stations based on multiple criteria and aggregate expert opinions.
4. **Risk Assessment**: Perform a risk analysis to identify the most vulnerable gas stations and suggest mitigation strategies.

## Project Phases
1. **Data Collection**: Gathering historical data on accidents and risk factors related to gas stations.
2. **Development of Evaluation Model**: Design and implement a multi-criteria decision-making model using the AHP methodology.
3. **Expert Evaluation System**: Build a web-based tool for collecting expert evaluations and processing them automatically.
4. **Final Analysis & Reporting**: Generate comprehensive vulnerability reports with visualizations and recommendations.

## Publications
- Published articles and conference papers detailing the methodology, results, and analysis of the vulnerability assessment model.

## Future Work
- **Model Refinement**: Further enhancement of the vulnerability assessment model by integrating additional data sources.
- **Broader Applications**: Extend the model to other critical infrastructure types, such as hospitals and power plants.
- **AI Integration**: Investigate the integration of machine learning algorithms to improve the accuracy and predictive capabilities of the assessment.

## Contributing
Contributions to the project are welcome. If you would like to contribute, please fork the repository and submit a pull request. Make sure to follow the guidelines for code quality and documentation.

