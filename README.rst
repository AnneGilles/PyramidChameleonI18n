PyramidChameleonI18n 
====================

I set up this project to test and demo the internationalization (i18n) features 
of Pyramid using Chameleon templates.


Problem & Solution
------------------
I did not get it to work. The translations were not picked up.

Thanks to wiggy from #pyramid, who spotted the mistake:

When specifying the i18n:domain in the template to be localized 
(i.e. have things translated) "the filename of the .mo file must match the 
domain exactely, including case."
