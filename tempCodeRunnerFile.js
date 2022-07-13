const Quiz = () => {
  var questions = [
    "What's your name?",
    "What's your age?",
    "What's your favorite color?",
  ];
  var options = [
    ["Mark", "Elone", "Magesh", "Adreiw"],
    [18, 19, 29, 22],
    ["Red", "Green", "Blue", "Yellow"],
  ];
  let que_idx = 0;
  const moveNext = () => {
    if (que_idx < questions.length - 1) {
      que_idx++;
    }
  };
  return (
    <View>
      <Text> Question</Text>
      {/* Question */}
      <Text>{questions[que_idx]}</Text>
      {/* Options */}
      {options[que_idx].map((option) => {
        return <Button
        >{option}</Button>;
      })}
    </View>
  );
};
