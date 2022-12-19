List<List<int>> Chunk(List<int> array, int size)
{
    var result = new List<List<int>>();
    var temp = new List<int>();

    array.ToList().ForEach(x =>
    {
        if (temp.Count.Equals(size))
        {
            result.Add(temp);
            temp.Clear();
        }
        temp.Add(x);
    });

    return result;
}

Chunk(new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }, 3);
Console.ReadKey();
