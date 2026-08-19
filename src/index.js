/**
 * TommyTech Platform Entry Point (JavaScript shim)
 * This file exists for CI linting compatibility.
 * The main application is in Python (src/main.py)
 */

module.exports = {
  name: 'tommytech-platform',
  version: process.env.TOMMTECH_VERSION || '0.1.0',
};
