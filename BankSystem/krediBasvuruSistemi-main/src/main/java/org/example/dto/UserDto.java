package org.example.dto;

public class UserDto {
    private String name;
    private Long identity;
    private String phone;
    private Long inCome;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Long getIdentity() {
        return identity;
    }

    public void setIdentity(Long identity) {
        this.identity = identity;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public Long getInCome() {
        return inCome;
    }

    public void setInCome(Long inCome) {
        this.inCome = inCome;
    }
}
