Tool=$(echo $1 |cut -d _ -f 1)
Mixture=$(echo $1 | cut -d _ -f 2)
Refrence=$(echo $1 | cut -d _ -f 3| cut -d . -f 1)

echo ${Mixture}_${Tool}_$Refrence
