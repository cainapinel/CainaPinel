# RPA News Extraction Challenge

## Overview

Our mission is to enable all people to do the best work of their lives—the first act in achieving that mission is to help companies automate tedious but critical business processes. This RPA challenge showcases your ability to build a bot for process automation.

## 🟢 The Challenge

My challenge was to automate the process of extracting data from a news site. The goal was to demonstrate the ability to build an RPA bot that can perform a series of automated actions to retrieve, process, and store news data.

## The Source

For this challenge, I used ONLY the Al Jazeera news website:

- https://www.aljazeera.com/

## Parameters

The process handles two main parameters via the Robocloud work item:

1. **news_topic**: A list of search phrases (in Python list format).
2. **period_months**: The number of months for which you need to receive news.

## Inputs Used in Control Room

- **news_topic**: `["climate change", "politics", "technology"]`
- **period_months**: `3`

These parameters were provided via a Robocloud work item, allowing dynamic control over the bot's search criteria and the time frame for retrieving news articles.

## The Process

### Main Steps:

1. **Open the site** by navigating to https://www.aljazeera.com/.
2. **Enter a phrase** in the search field and initiate the search.
3. On the result page:
    - **Select a news category or section** from the available options if applicable.
    - **Choose the latest news** articles.
4. **Extract the following values** for each article:
    - Title
    - Date
    - Description
    - Picture filename
    - Count of search phrases in the title and description
    - True or False, depending on whether the title or description contains any amount of money

    Possible formats for amounts of money:
    - $11.1
    - $111,111.11
    - 11 dollars
    - 11 USD

5. **Store the extracted data** in an Excel file with columns:
    - Title
    - Date
    - Description
    - Picture filename
    - Count of search phrases in the title and description
    - True or False for the presence of monetary amounts
6. **Download the news picture** and specify the file name in the Excel file.
7. **Repeat steps 4-6** for all news articles that fall within the required time period.

## Implementation Details

### Setting Up Robocorp Control Room

1. **Clone the Repository**:
    ```bash
    git clone [your-public-repo-link]
    cd [your-repo-directory]
    ```

2. **Create a Robocorp Control Room Process**:
    - Follow the [Robocorp Control Room setup guide](https://robocorp.com/docs/courses/beginners-course-python/12-running-in-robocorp-cloud).
    - Create a new process in Robocorp Control Room.
    - Upload your code to the process.

3. **Configure Parameters in Robocorp**:
    - Define the `news_topic` and `period_months` parameters within the Robocloud work item.
    - Example configuration:
        ```json
        {
            "news_topic": ["climate change", "politics", "technology"],
            "period_months": 3
        }
        ```

4. **Ensure Successful Run**:
    - Run the process and ensure it completes successfully.
    - Write the output files to the `/output` directory to make them visible in the artifacts list.

5. **Invite Reviewers**:
    - Once completed, invite [Challenges@thoughtfulautomation.com](mailto:Challenges@thoughtfulautomation.com) to your Robocorp Org.

## Output

The output is an Excel file stored in the `/output` directory containing the extracted news data with the following columns:

- Title
- Date
- Description
- Picture filename
- Count of search phrases in the title and description
- True or False for the presence of monetary amounts

Additionally, the images downloaded from the news articles are stored in the same directory.

## Conclusion

This challenge demonstrates the ability to automate data extraction from the Al Jazeera news site using RPA tools and techniques. The solution handles parameterized inputs, processes the data, and stores the results efficiently.

---

Feel free to reach out for any clarifications or further assistance.
