# Mermaid ：Directive Examples 

https://mermaid.js.org/config/directives.html#directive-examples

Now that the concept of directives has been explained, let us see some more examples of directive usage:
Changing theme via directive

The following code snippet changes theme to forest:

%%{init: { "theme": "forest" } }%%

Possible theme values are: default, base, dark, forest and neutral. Default Value is default.

Example:

Code:

```
%%{init: { "theme": "forest" } }%%
graph TD
A(Forest) --> B[/Another/]
A --> C[End]
  subgraph section
  B
  C
  end
```



