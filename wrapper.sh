#!/bin/bash
for csv in private/*.csv; do
        # delete timestamp column if present
        if [ "$(head -n1 < $csv | cut -d , -f 1)" == "Timestamp" ]; then
                cp $csv $csv.old #make backup
                cut -d , -f 2- <$csv.old >$csv
                rm $csv.old #rm backup
                echo Removed timestamps from $csv
        fi

        # serialize names of genres to integer values
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

echo
echo "finished running script, exiting now"
