# call by value VS call by reference  
메소드에서 인자값을 호출할 때, 받아오는 방식에 구분.

### 1. call by value  
값에 의한 호출의 의미로, 호출시 인자의 메모리에 저장되어 있는 값을 복사하여 받는다.  
메소드 내에서는 복사된 값으로 작업을 하기 때문에, 원래의 값을 변경시키지 않는다.  
``` c
void swap(int v1, int v2) {
	int tmp = 0;
	tmp = v1;
	v1 = v2;
	v2 = tmp;
}

void main() {
	int x=10, y=20;
	swap(x, y);
	printf("%d %d\n", x, y);
	return;
}
```

### 2. call by reference  
참조에 의한 호출의 의미로, 호출시 인자 값의 메모리에 저장되어 있는 주소를 복사하여 받는다.  
객체를 참조하는 주소를 넘겨받기 때문에, 메소드 내에서도 원래의 값에 접근이 가능하다.
``` c
void swap(int *v1, int *v2) {
	int tmp = 0;
	tmp = *v1;
	*v1 = *v2;
	*v2 = tmp;
}

void main() {
	int x=10, y=20;
	swap(&x, &y);
	printf("%d %d\n", x, y);
	return;
}
```

### 3. 자바에서의 관점
자바에서는 call by value 형식으로 호출하지만, reference 형식으로 호출한다고 생각하게 한다.   
자바는 기본형 타입 변수와 참조형 타입 변수가 있는데, 기본형 타입은 값을 복사해서 전달받고 참조형 타입은 값의 래퍼런스를 복사해서 전달받는다.  
(세터함수를 이용한 내부의 멤버변수를 바꾸는 예제는, 복사된 래퍼런스 내부 필드의 값을 단순하게 변경한 것이다.)  

### 참고  
1. [자바의 메소드(함수) 호출 방식](https://siyoon210.tistory.com/104)  
2. [자바 Call by value Call by reference](https://sleepyeyes.tistory.com/11) 
3. [Call by value & Call by reference](https://hyoje420.tistory.com/6)  
4. [Java 인자 전달 방식](http://mussebio.blogspot.com/2012/05/java-call-by-valuereference.html)  
5. [Call by Value or Reference in JAVA](https://history1994.tistory.com/8?category=668240)  

