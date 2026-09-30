class CountryComparator implements Comparator<Country> {
    @Override
    public int compare(Country c1, Country c2) {
        //compare by population
        if (c1.population < c2.population) {
            return -1;
        } else if (c1.population > c2.population) {
            return 1;
        } else {
            return 0;
        }
    }
}