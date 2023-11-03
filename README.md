# Web Wordlists

This project provides a collection of **curated wordlists optimized for web pentesting**. It can help you during the discovery part, or to bypass a WAF by finding an unfiltered keyword.

## Drupal

**Scenario:** Use the plugins list to discover which plugins are installed on the targeted Drupal server.

- [drupal_modules_list.txt](./drupal/drupal_modules_list.txt): List of all Drupal modules from [www.drupal.org](https://www.drupal.org/project/project_module), sort by *Most installed*.
- [drupal_modules_path.txt](./drupal/drupal_modules_path.txt): Same as `drupal_modules_list.txt` but with the prefix `/modules/` to match real URL of modules. 

## HTML

**Scenario:** Use the HTML tags/events list to enumerate which tags/events are allowed/blocked by a WAF.

- [html_tags.txt](./html/html_tags.txt): List of all HTML tags.
- [html_events.txt](./html/html_events.txt): List of all HTML javascript events.

## SQL Keywords

**Scenario:** Use the SQL keywords list to enumerate which keywords are allowed/blocked by a WAF.

- [mysql_keywords.txt](sql/mysql_keywords.txt): List of all SQL keywords based on [dev.mysql.com](https://dev.mysql.com/doc/refman/8.0/en/keywords.html).