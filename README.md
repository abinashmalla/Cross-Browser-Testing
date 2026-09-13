<!-- ========================================== -->
<!--           CROSS-BROWSER TESTING            -->
<!-- ========================================== -->

## 🌐 Cross-Browser Testing

To deliver a consistent user experience, this application is continuously tested across all major modern browsers, operating systems, and viewport sizes.

<br />

## https://drive.google.com/file/d/11Afxji1y5zzhOatjOSSB86Y023vK38Ba/view?usp=sharing

### 💻 Supported Browsers & Environments

| Browser | Version / Engine | Windows | macOS | Linux | iOS | Android |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Google Chrome** | Latest 2 versions |  |  |  |  |  |
| **Mozilla Firefox** | Latest 2 versions |  |  |  | ➖ | ➖ |
| **Apple Safari** | 15+ (WebKit) | ❌ |  | ❌ |  | ❌ |
| **Microsoft Edge** | Latest 2 versions |  |  |  |  |  |
| **Brave** | Chromium-based |  |  |  |  |  |

* Legend: Supported |  Not Available / Untested | ➖ Limited Support*

---

### 🧪 Automated E2E & Visual Testing

We use **[Playwright](https://playwright.dev/)** / **[Cypress](https://www.cypress.io/)** for automated end-to-end testing across matrix configurations.

```bash
# Run cross-browser tests locally
npm run test:e2e

# Run tests against a specific browser engine
npm run test:e2e -- --project=chromium
npm run test:e2e -- --project=firefox
npm run test:e2e -- --project=webkit
