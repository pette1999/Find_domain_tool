const chrome = require('selenium-webdriver/chrome');
const firefox = require('selenium-webdriver/firefox');
const { Builder, By, Key, util } = require("selenium-webdriver");

async function findDomain() {
    //let driver = await new Builder().forBrowser("chrome").setChromeOptions(new chrome.Options().headless()).build();
    let driver = await new Builder().forBrowser("chrome").build();
    await driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin");
    await console.log("Connecting to Linkedin.com...");
    await driver.findElement(By.xpath("//*[@id='username']")).sendKeys("1932807205@qq.com");
    await driver.findElement(By.xpath("//*[@id='password']")).sendKeys("Meiguo1969", Key.RETURN);
    await console.log("Logging in...");
    console.log(await driver.getCurrentUrl());
}

// return all the links in an array
function readLink() {
    const fs = require('fs')
    
    try {
        const data = fs.readFileSync("../link.txt", "UTF-8");
        const lines = data.split(/\r?\n/);

        lines.forEach(line => {
            line = line.trim();
        });

        return lines;
    } catch (error) {
        console.error(error);
    }
}

async function getLinkLength() {
    console.log(readLink().length);
    //return readLink().length;
}

getLinkLength();