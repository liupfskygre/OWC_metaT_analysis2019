# this part of data is downloaed by adrienne

#url: https://genome.jgi.doe.gov/portal/Frogenwetlasoils/Frogenwetlasoils.info.html


#metaT2018JGI_reads_partIII_list.txt

#report

```
#on zenith
mkdir filtered-report
cd filtered-report

grep -E 'Old\ Woman\ Creek\ 2018\ metatranscriptomes|Old\ Woman\ Creek\ Soil\ metatranscriptomes' get-directory.xml > get-directory_metaT2018partIII.xml
#

sed -e 's/.* \(label=.*\) filename=.* \(url=.*\) project=.*$/\1\t\2/g' get-directory_metaT2018partIII.xml >get-directory_metaT2018partIII_link.xml

sed -i -e 's/.*metatranscriptomes \(.*\)".*url=.*\(url=.*\)"$/\1\t\2/g' get-directory_metaT2018partIII_link.xml
sed -i -e 's/url=//g' get-directory_metaT2018partIII_link.xml

grep 'filtered-report' get-directory_metaT2018partIII_link.xml >get-directory_metaT2018partIII_link.report

sed -i -e 's/\t/;/g' get-directory_metaT2018partIII_link.report

grep -w -f metaT2018JGI_reads_partIII_list0.txt get-directory_metaT2018partIII_link.report > get-directory_metaT2018partIII_link10.report

#transfer to zenith and download

for line in $(cat get-directory_metaT2018partIII_link10.report)
do
echo "${line}" # '\t' cause problem
v1="$(echo "${line}"|cut -f2 -d';')"
echo "${v1}"
v2="$(echo "${line}"|cut -f1 -d$';')"
echo "${v2}"

curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=newlifesky19870720' -c cookies > /dev/null

curl "https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=${v1}" -b cookies > "${v2}".filtered-report.txt
done

grep 'Output' *.filtered-report.txt> metaT2018partIII_filtered-report_summary.txt
```
