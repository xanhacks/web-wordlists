# Web Wordlists

This project provides a collection of curated wordlists optimized for web enumeration tasks.

## Drupal

Scenario: Use the plugins list to discover which plugins are installed on the targeted Drupal server.

- [drupal_modules_list.txt](./drupal/drupal_modules_list.txt): List of all Drupal modules from [www.drupal.org](https://www.drupal.org/project/project_module), sort by *Most installed*.
- [drupal_modules_path.txt](./drupal/drupal_modules_path.txt): Same as `drupal_modules_list.txt` but with the prefix `/modules/` to match real URL of modules. 

## HTML

Scenario: Use the HTML tags/events list to enumerate which tags/events are blocked by a WAF.

- [html_tags.txt](./html/html_tags.txt): List of all HTML tags.
- [html_events.txt](./html/html_events.txt): List of all HTML javascript events.
