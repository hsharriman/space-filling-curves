"""Generate a Sierpiński Square Snowflake."""


def sierp_pt2code( double ax, double ay, double bx, double by, double cx, double cy,
    int currentLevel, int maxLevel, long code, double x, double y ) 
{
    if (currentLevel <= maxLevel) {
        currentLevel++;
        if ((sqr(x-ax) + sqr(y-ay)) < (sqr(x-cx) + sqr(y-cy))) {
            code = sierp_pt2code( ax, ay, (ax+cx)/2.0, (ay+cy)/2.0, bx, by,
                currentLevel, maxLevel, 2 * code + 0, x, y );
        }
        else {
            code = sierp_pt2code( bx, by, (ax+cx)/2.0, (ay+cy)/2.0, cx, cy,
                currentLevel, maxLevel, 2 * code + 1, x, y );
        }
    }   
    return code;    
}

def main():
    pass


if __name__ == __main__:
    main()