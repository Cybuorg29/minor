#import <Foundation/Foundation.h>

@interface Person : NSObject

@property NSString *name;
@property NSUInteger age;
@property CGFloat height;

- (instancetype)initWithName:(NSString *)name age:(NSUInteger)age height:(CGFloat)height;

@end

#import "Person.h"

@implementation Person

- (instancetype)initWithName:(NSString *)name age:(NSUInteger)age height:(CGFloat)height
{
    self = [super init];
    if (self) {
        self.name = name;
        self.age = age;
        self.height = height;
    }
    return self;
}

@end