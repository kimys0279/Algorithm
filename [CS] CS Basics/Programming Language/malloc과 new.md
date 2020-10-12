# malloc과 new

공통점 

-메모리를 동적할당할때 사용

차이점

**-malloc은 라이브러리에서 제공하는 함수, new는 연산자다.**

malloc은 c언어에서 동적할당을 하기위해서 사용하는 함수로 stdlib.h 헤더파일에 포함되어있다.

할당할 대상의 크기를 전달해야하고, 반환형이 void형 포인터이기때문에 형 변환을 거쳐야한다.

new는 c++에서 제공하는 연산자로 헤더파일 추가없이 사용가능하다.

메모리의 사이즈와 형식을 지정해 해당 타입의 포인터를 반환해준다.

**-malloc은 생성자를 호출하지 않지만, new는 생성자를 자동 호출한다.**

가장 중요한 차이점으로 객체를 동적할당시 malloc은 단순히 메모리만 할당되고 생성자를 호출하지 않고 new는 생성자를 호출하여 메모리를 할당한다.

**-new는 메모리할당과 동시에 초기화가 가능, malloc은 불가능하다.**

**-new는 delete연산자를 사용해서 메모리해제, malloc은 free함수로 메모리해제**

delete연산자는 메모리해제시 소멸자를 호출, free함수는 소멸자를 호출하지않음

```cpp
#include <iostream>
using namespace std;
class test
{
public:
	test()
	{
		cout << "test" << endl;
	}
	~test()
	{
		cout << "test destroyed" << endl;
	}
};

int main()
{
	cout << "malloc / free의 경우" << endl;
	test* m_ptr = (test*)malloc(sizeof(test));
	free(m_ptr);
	cout << endl;

	cout << "new / delete의 경우" << endl;
	test* n_ptr = new test;
	delete n_ptr;
	cout << endl;

	return 0;
}
```

![캡처](https://user-images.githubusercontent.com/37561621/89129870-ce59cd80-d53b-11ea-8c7e-7a9aff32a54e.PNG)


참고

```cpp
int *p = new int[10];
delete[] p;
```
배열객체를 해제할때는 delete[] 를 사용해서 해제해야한다

delete p; 로 해제 할경우 p[0]에 대한 소멸자만 호출돼서 p[0]만 메모리해제되기 때문에 메모리누수가 발생한다.


**-malloc은 realloc 함수를 이용해서 사이즈 재할당이 가능하다.**

malloc은 realloc함수를 이용해서 재할당이 가능하다. 

new는 새로운 메모리를 할당해서 복사한뒤 해제를 해야돼서 재할당을 많이하는경우에는 malloc이 효율적일수도있다.

realloc()시 발생할 수 있는 문제점

재할당실패시 null 반환하기 때문에 기존의 메모리 포인터 잃어버린다.

realloc()시 기존메모리 저장 후 실패시 다시 복구해줄수 있어야한다.

추가) realloc() 함수는 만약 기존의 메모리 위치에 충분한 공간이 있다면 바로 이어서 추가 메모리 공간을 할당해 준다.

기존의 메모리 위치에 충분한 공간이 없으면 메모리의 다른 공간에 기존의 데이터를 복사한 후, 이어서 추가 메모리 공간을 할당하게 되고

이것도 실패하게되면 메모리 재할당이 실패해서 null을 반환하게된다.
