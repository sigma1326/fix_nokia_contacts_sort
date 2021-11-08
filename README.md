# Fix Nokia Contact Sorting Issue in RM-1137 and RM-1136 Models

A fix for importing contacts from older Nokia phones to models like RM-1137 and RM-1136 which
the sorting in contacts list is based on last name. After the convertion is finished the `out.vcf` file must be renamed to `backup.dat` and placed
in the `backup` folder of the phone's sd-card. Now the contacts can be restored via `backup` menu in `settings`.
