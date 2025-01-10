import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_main_page_data(driver):

    load_more_btn_xpath = "/html/body/div[1]/div[5]/div[2]/div[2]/button"
    match_container_xpath = "/html/body/div[1]/div[5]/div[2]/div[2]/div[3]/div"

    wait = WebDriverWait(driver, 10)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"match_data_{timestamp}.txt"

    while True:
        try:
            load_more_btn = wait.until(EC.element_to_be_clickable((By.XPATH, load_more_btn_xpath)))
            load_more_btn.click()
            time.sleep(2)
        except:
            break

    matches = driver.find_elements(By.XPATH, match_container_xpath)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Tarih,K/D/A,KDA,LP,CS,Lig\n")
        for idx, match in enumerate(matches, start=1):
            try:
                time_str = match.find_element(By.XPATH, ".//div/div[2]/div/div[1]/div[1]/div[2]/div").text.strip()
                match_date_str = time_str
            except Exception as e:
                match_date_str = "N/A"

            try:
                kills = match.find_element(By.XPATH, ".//div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[1]").text.strip()
                deaths = match.find_element(By.XPATH, ".//div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[2]").text.strip()
                assists = match.find_element(By.XPATH, ".//div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[3]").text.strip()
                kda = match.find_element(By.XPATH, ".//div/div[2]/div/div[2]/div[1]/div[2]/div[2]").text.strip()
                lp = match.find_element(By.XPATH, ".//div/div[2]/div/div[2]/div[1]/div[3]/div[2]").text.strip()
                cs = match.find_element(By.XPATH, ".//div/div[2]/div/div[2]/div[1]/div[3]/div[3]/div").text.strip()
                lig = match.find_element(By.XPATH, ".//div/div[2]/div/div[2]/div[1]/div[3]/div[4]/div").text.strip()
            except:
                kills, deaths, assists, kda, lp, cs, lig = "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"

            file.write(f"{match_date_str},{kills}/{deaths}/{assists},{kda},{lp},{cs},{lig}\n")
            print(f"{idx}. Tarih={match_date_str}, KDA={kda}, LP={lp}, CS={cs}, Lig={lig}")

def scrape_champions_data(driver):
    
    champions_tab_xpath = "/html/body/div[1]/div[2]/div[2]/ul/li[2]/a/div"
    wait = WebDriverWait(driver, 10)
    champs_tab = wait.until(EC.element_to_be_clickable((By.XPATH, champions_tab_xpath)))
    champs_tab.click()
    time.sleep(3)

    season_open_btn_xpath = "/html/body/div[1]/div[5]/div/div/div[1]/div[2]/div[2]/div/button"
    season_list = ["Sezon 2024 S3", "Sezon 2024 S2", "Sezon 2024 S1"]

    for season_text in season_list:

        open_btn = wait.until(EC.element_to_be_clickable((By.XPATH, season_open_btn_xpath)))
        open_btn.click()
        time.sleep(1)

        season_btn_xpath = f"//button[contains(text(),'{season_text}')]"
        try:
            season_btn = wait.until(EC.element_to_be_clickable((By.XPATH, season_btn_xpath)))
            season_btn.click()
            time.sleep(3)
        except Exception as e:
            continue

        row_xpath_base = "/html/body/div[1]/div[5]/div/table/tbody/tr"
        table_rows = driver.find_elements(By.XPATH, row_xpath_base)
        wanted_rows = [row for row in table_rows if "css-1685pqm e1uh0vzh2" not in row.get_attribute("class")]

        output_file = season_text.replace(" ", "_") + ".txt"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("Rank,Champion,Wins,Losses,Win Rate,KDA\n")
            for i, row in enumerate(wanted_rows, start=1):
                try:
                    rank = row.find_element(By.XPATH, "./td[1]").text.strip()
                    champ = row.find_element(By.XPATH, "./td[2]/div/div[2]/a").text.strip()

                    try:
                        wins = row.find_element(By.XPATH, "./td[3]/div/div/div[contains(@class, 'winratio-graph__text left')]").text.strip()
                    except:
                        wins = "0G"  

                    try:
                        loses = row.find_element(By.XPATH, "./td[3]/div/div/div[contains(@class, 'winratio-graph__text right')]").text.strip()
                    except:
                        loses = "0Y" 

                    ratio = row.find_element(By.XPATH, "./td[3]/div/span").text.strip()
                    kda = row.find_element(By.XPATH, "./td[4]/div/strong").text.strip()
                except:
                    rank, champ, wins, loses, ratio, kda = "N/A", "N/A", "0G", "0Y", "N/A", "N/A"

                file.write(f"{i}. Rank={rank}, Champ={champ}, Wins={wins}, Losses={loses}, Ratio={ratio}, KDA={kda}\n")
                print(f"{i}. Rank={rank}, Champ={champ}, Wins={wins}, Losses={loses}, Ratio={ratio}, KDA={kda}")

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        base_url = "https://www.op.gg/summoners/euw/ThanksForDiana-EUW"
        driver.get(base_url)
        time.sleep(3)

        scrape_main_page_data(driver)
        scrape_champions_data(driver)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
