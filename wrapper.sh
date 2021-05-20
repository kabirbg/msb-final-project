#!/usr/bin/env sh

for csv in private/*.csv; do
        # delete timestamp column if present
        if [ "$(head -n1 < "$csv" | cut -d ',' -f 1)" = "Timestamp" ]; then
                cp "$csv" "${csv}.old" #make backup
                cut -d ',' -f 2- <"${csv}.old" >"$csv"
                rm "${csv}.old" #rm backup
                printf 'Removed timestamps from %s\n' "$csv"
        fi

        # serialize names of genres to integer values
        sed -i '' 's/Pop/1/g' "$csv" && printf "replaced 'pop' with '1' in %s\n" "$csv"
        sed -i '' 's/Jazz\/Blues/2/g' "$csv" && printf "replaced 'jazz/blues' with '2' in %s\n" "$csv"
        sed -i '' 's/Rock/3/g' "$csv" && printf "replaced 'rock' with '3' in %s\n" "$csv"
        sed -i '' 's/Country\/Folk/4/g' "$csv" && printf "replaced 'country/folk' with '4' in %s\n" "$csv"
        sed -i '' 's/Rap\/Hip Hop/5/g' "$csv" && printf "replaced 'rap/hip hop' with '5' in %s\n" "$csv"
        sed -i '' 's/Classical/6/g' "$csv" && printf "replaced 'classical' with '6' in %s\n" "$csv"
        sed -i '' 's/Dislike/0/g' "$csv" && printf "replaced 'dislike' with '0' in %s\n" "$csv"
        sed -i '' 's/Like/1/g' "$csv" && printf "replaced 'like' with '1' in %s\n" "$csv"
        printf 'finished working on %s\n\n' "$csv"
done
python3 main.py

printf '\nfinished running script, exiting now\n'
