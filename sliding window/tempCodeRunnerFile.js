const fetchData = async () => {
  const response = await fetch("https://fakestoreapi.com/products").then(
    (res) => console.log(res.data)
  );
  console.log(response);
};

fetchData();
