const { chromium } = require('playwright');
const path = require('path');

(async () => {
  // Launch browser
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  // Set viewport size to match design
  await page.setViewportSize({ width: 1400, height: 900 });
  
  // Load our HTML file
  const htmlPath = path.join(__dirname, 'frontend', 'demo.html');
  await page.goto(`file://${htmlPath}`);
  
  // Wait for content to load
  await page.waitForTimeout(1000);
  
  // Take full page screenshot
  await page.screenshot({ 
    path: 'implementation-screenshot.png', 
    fullPage: true 
  });
  
  console.log('Screenshot taken: implementation-screenshot.png');
  
  await browser.close();
})();