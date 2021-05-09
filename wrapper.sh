#!/bin/bash
for csv in private/*.csv; do
        if [ "$(head -n1 < Family.csv | awk '{print $1}')" == "Timestamp" ]; then
                gawk -i inplace -F "\"*,\"*" '{$1="";print $0}' private/Family.csv && echo Removed timestamps from $csv
        fi
        sed -i '' 's/Pop/1/g' $csv && echo replaced 'pop' with '1' in $csv
        sed -I '' 's/Jazz\/Blues/2/g' $csv && echo replaced 'jazz/blues' with '2' in $csv
        sed -I '' 's/Rock/3/g' $csv && echo replaced 'rock' with '3' in $csv
        sed -I '' 's/Country\/Folk/4/g' $csv && echo replaced 'country/folk' with '4' in $csv
        sed -I '' 's/Rap\/Hip Hop/5/g' $csv && echo replaced 'rap/hip hop' with '5' in $csv
        sed -I '' 's/Classical/6/g' $csv && echo replaced 'classical' with '6' in $csv
        sed -I '' 's/Dislike/0/g' $csv && echo replaced 'dislike' with 0 in $csv
        sed -I '' 's/Like/1/g' $csv && echo replaced 'like' with 1 in $csv
        echo -e "finished working on $csv\n"
done
python3 main.py
echo -e "\nfinished running script, exiting now"
